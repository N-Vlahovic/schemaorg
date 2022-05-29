import datetime
import json
import os
import re
import shutil

import utils


DEFAULT_CURRENT_ONLY: bool = False
DEFAULT_FIELDS: dict = {}
DEFAULT_FIELD_TYPE: list = ["AbstractBase"]
DEFAULT_PARENT: list[str] = ["AbstractBase"]
TAB: str = " " * 4
MODELS_DIR_PATH: str = f"{utils.MODULE_PATH}/models"
SINGLE_MODELS_FILE: str = f"{MODELS_DIR_PATH}/all_models.py"
HTTPS_JSON: str = "schemaorg-%s-https.jsonld"
BUILTINS_MAPPING: dict = {
    "Boolean": bool,
    "Date": datetime.date,
    "DateTime": datetime.datetime,
    "Number": float | int,
    "Text": str,
    "Time": datetime.time
}


def get_last_release_version() -> str:
    hist = {}
    with open(f"{utils.PROJECT_PATH}/versions.json", "r", encoding="utf-8") as _:
        for v, d in json.loads(_.read()).get("releaseLog", {}).items():
            try:
                d = datetime.datetime.fromisoformat(d)
                hist[d] = v
            except ValueError:
                continue
    return hist[max(hist)]


def get_latest_release_data(current_only: bool = DEFAULT_CURRENT_ONLY) -> dict:
    v = get_last_release_version()
    file_name = HTTPS_JSON % ("current" if current_only else "all")
    with open(f"{utils.PROJECT_PATH}/data/releases/{v}/{file_name}", "r", encoding="utf-8") as _:
        return json.loads(_.read())


def dict_update(data0: dict, data1: dict) -> dict:
    data = {}
    for key in sorted(set(data0) | set(data1)):
        val0, val1 = data0.get(key), data1.get(key)
        val = val0 if val0 else val1
        t0, t1 = type(val0), type(val1)
        if val0 and val1 and t0 == t1:
            if isinstance(val0, dict):
                val = dict_update(val0, val1)
            elif isinstance(val0, list):
                val = val0 + val1
            elif isinstance(val0, set):
                val = val0 | val1
        data.update({key: val})
    return data


def update_helper(data: dict, key: str, **kwargs) -> None:
    data.update({
        key: dict_update(
            data.get(key, {}),
            kwargs
        )
    })


def includes_helper(include: list[dict] | dict) -> list[str]:
    include = include if isinstance(include, list) else [include]
    return list(filter(lambda _: _.lower() != "class", sorted(id_cleaner(_.get("@id")) for _ in include if _)))


def id_cleaner(string: str) -> str:
    return re.sub(r"^schema:(.*)", r"\1", string)


def camel_to_snake(name: str) -> str:
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    name = re.sub(r'([a-z\d])([A-Z])', r'\1_\2', name).lower()
    # name = f"s_{name}"
    return name


def get_last_release_schema_definitions(current_only: bool = DEFAULT_CURRENT_ONLY) -> tuple[dict, dict, dict]:
    graph = get_latest_release_data(current_only).get("@graph", {})
    classes, properties, schemas = {}, {}, {}
    for d in graph:
        _id = id_cleaner(d.get("@id"))
        _type = d.get("@type")
        label = d.get("rdfs:label")
        types = _type if isinstance(_type, list) else [_type]
        for t in types:
            if t == "rdfs:Class":
                update_helper(
                    classes,
                    _id,
                    name=label,
                    id=_id,
                    parents=includes_helper(d.get("rdfs:subClassOf"))
                )
            elif t == "rdf:Property":
                domain_includes = includes_helper(d.get("schema:domainIncludes"))
                range_includes = includes_helper(d.get("schema:rangeIncludes"))
                update_helper(
                    properties,
                    _id,
                    name=label,
                    id=_id,
                    domain_includes=domain_includes,
                    range_includes=range_includes
                )
                for di in domain_includes:
                    update_helper(
                        classes,
                        di,
                        id=di,
                        fields={_id: range_includes or DEFAULT_FIELD_TYPE}
                    )
            elif re.fullmatch(r"^schema:.*", t):
                update_helper(
                    schemas,
                    _id,
                    **d
                )
            else:
                raise ValueError(f"Unknown type {t}")
    return classes, properties, schemas


def get_genealogy_helper(data: dict, key: str, out: list = None):
    out = out or []
    if ancestors := data.get(key, {}).get("parents", []):
        for _ in ancestors:
            out += get_genealogy_helper(data, _, [_])
    return out


def get_genealogy(current_only: bool = DEFAULT_CURRENT_ONLY) -> dict:
    data = get_last_release_schema_definitions(current_only)[0]
    genealogy = {}
    for key in data:
        tmp = genealogy
        for _ in reversed(get_genealogy_helper(data, key)):
            if _ not in tmp:
                tmp[_] = {}
            tmp = tmp[_]
        tmp[key] = {}
    return genealogy


def write_model_file(
        file_name: str,
        body: str = None,
        imports: str = None,
) -> None:
    code = model_file_header()
    imports = "from __future__ import annotations\n" + (imports if imports else "")
    code += f"{imports}\n"
    if body:
        code += f"\n\n{body}"
    with open(file_name, "w", encoding="utf-8") as _:
        _.write(code)


def generate_abstract_base() -> None:
    name = "AbstractBase"
    write_model_file(
        file_name=f"{MODELS_DIR_PATH}/{camel_to_snake(name)}.py",
        body=f"@dataclass\nclass {name}:\n{TAB}pass\n",
        imports="from dataclasses import dataclass"
    )


def generate_model_body(name: str, fields: dict, parents: list, single_file: bool = False) -> str:
    def helper0(s: str) -> str:
        return s if single_file is True else f"{camel_to_snake(s)}.{s}"

    body = f"@dataclass\nclass {name}(%s):\n" % ", ".join(map(helper0, parents))
    if fields:
        for key, val in fields.items():
            body += f"{TAB}{key}: %s | None = None\n" % " | ".join(helper0(_) if _ != name else _ for _ in val)
    else:
        body += f"{TAB}pass\n"
    return body


def get_model_file_data(data: dict, single_file: bool = False) -> tuple:
    _id = camel_to_snake(data["id"])
    name = data["name"]
    name = name.get("@value") if isinstance(name, dict) else name
    if not name:
        raise NameError(f"Unsupported name {name}")
    fields = data.get("fields") or {}
    parents = [_ for _ in data.get("parents") or [] if _ not in ["rdfs:Class"]] or DEFAULT_PARENT
    file_name = f"{MODELS_DIR_PATH}/{_id}.py"
    to_import = set(parents) | {_ for _ in fields.values() for _ in _}
    imports = "from dataclasses import dataclass\n\n"
    imports += "\n".join(
        f"import models.{camel_to_snake(_)} as {camel_to_snake(_)}" for _ in sorted(to_import.difference({name}))
    )
    body = generate_model_body(name=name, fields=fields, parents=parents, single_file=single_file)
    return body, imports, file_name


def generate_model(data: dict) -> None:
    body, imports, file_name = get_model_file_data(data, single_file=False)
    write_model_file(
        file_name=file_name,
        body=body,
        imports=imports
    )


def model_file_header() -> str:
    code = '# !/usr/bin/env python3\n# -*- coding: utf-8 -*-\n'
    code += f'# Auto-generated on {datetime.datetime.utcnow().isoformat()}\n'
    code += f'# For more info concerning Schema.org c.f. https://schema.org/\n'
    code += f'# For more info concerning this script c.f. nikolai@nexup.com\n'
    return code


def init_models_dir() -> None:
    shutil.rmtree(MODELS_DIR_PATH)
    os.makedirs(MODELS_DIR_PATH, exist_ok=True)
    with open(f"{MODELS_DIR_PATH}/__init__.py", "w", encoding="utf-8") as _:
        _.write(model_file_header())
    generate_abstract_base()


def genealogy_to_code(genealogy: dict, data: dict, body: str):
    body += "\n\n".join(get_model_file_data(data=data.pop(key), single_file=True)[0] for key in genealogy if key in data)
    return body


def generate_all_models(single_file: bool = True, current_only: bool = DEFAULT_CURRENT_ONLY):
    data = get_last_release_schema_definitions(current_only)[0]
    init_models_dir()
    if single_file is False:
        for key, val in data.items():
            generate_model(val)
        return
    tree = utils.get_model_tree([v for k, v in data.items() if k != "rdfs:Clas"])
    body = "\n\n".join(get_model_file_data(_.asdict(), True)[0] for _ in tree)
    header = model_file_header()
    imports = "from __future__ import annotations\nfrom dataclasses import dataclass\n\n" \
              "from models.abstract_base import AbstractBase"
    code = f"{header}\n{imports}\n\n{body}"
    with open(SINGLE_MODELS_FILE, "w", encoding="utf-8") as _:
        _.write(code)


def save_schema_files(path: str, current_only: bool = DEFAULT_CURRENT_ONLY) -> None:
    classes, properties, schemas = get_last_release_schema_definitions(current_only)
    for name, data in [
        ("classes", classes),
        ("properties", properties),
        ("schemas", schemas),
        ("noFields", {k: v for k, v in classes.items() if v.get("fields") is None and not v.get("parents")})
    ]:
        print(name)
        with open(f"{path}/{name}.json", "w", encoding="utf-8") as _:
            json.dump({k: data[k] for k in sorted(data)}, _)
    print("OK")


if __name__ == '__main__':
    save_schema_files(os.path.expanduser("~"))
    generate_all_models()
