from __future__ import annotations

import re
from dataclasses import dataclass, field, asdict
from typing import Iterable
import os
from pathlib import Path


MODULE_PATH: Path = Path(os.path.dirname(os.path.abspath(__file__)))
PROJECT_PATH: Path = MODULE_PATH.parent.parent
RESERVED_NAMES: set[str] = {
    "yield", "next", "in", "if", "while", "continue", "for", "from", "import", "class", "def", "break", "return"
}


def name_handler(name: str) -> str:
    if name in RESERVED_NAMES:
        return name + "_"
    if re.fullmatch(r"^\d.*", name):
        return "d_" + name
    return name


@dataclass
class Node:
    id: str
    children: list[Node | str] = field(default_factory=list)
    parents: list[Node | str] = field(default_factory=list)
    fields: dict[str, list] = field(default_factory=dict)

    def __eq__(self, other: Node) -> bool:
        return self.id == (other if isinstance(other, str) else other.id)

    def asdict(self) -> dict:
        return asdict(self) | {"name": self.id}


def get_model_nodes(data: Iterable[dict]) -> list[Node]:
    nodes = []
    for d in data:
        _id = d["id"]
        children = [_["id"] for _ in data if _id in (_["parents"] or [])]
        nodes.append(Node(
            id=name_handler(_id),
            children=list(map(name_handler, children)),
            parents=[name_handler(_) for _ in d["parents"] or [] if _ != "rdfs:Class"],
            fields={name_handler(k): list(map(name_handler, v)) for k, v in (d.get("fields") or {}).items()}
        ))
    return sorted(nodes, key=lambda _: len(_.parents))


def get_model_tree(data: Iterable[dict]) -> list[Node]:
    tree = []
    nodes = sorted(get_model_nodes(data), key=lambda _: len([_ for _ in _.parents if _ not in tree]))
    while nodes:
        n = nodes.pop(0)
        if all(_ in tree for _ in n.parents):
            tree.append(n)
            for c in n.children:
                try:
                    tree.index(c)
                except ValueError:
                    c = nodes[nodes.index(c)]
                if c not in tree and all(_ in tree for _ in c.parents):
                    tree.append(nodes.pop(nodes.index(c)))
        else:
            nodes.append(n)
            print(n)
        nodes = sorted(nodes, key=lambda _: len([_ for _ in _.parents if _ not in tree]))
    return tree
