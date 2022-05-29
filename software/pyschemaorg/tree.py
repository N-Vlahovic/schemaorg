from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Node:
    id: str
    children: list[Node | str] = field(default_factory=list)
    parents: list[Node | str] = field(default_factory=list)
    fields: list[dict] = field(default_factory=list)

    def __eq__(self, other: Node) -> bool:
        return self.id == (other if isinstance(other, str) else other.id)


def get_model_nodes(data: list[dict]) -> list[Node]:
    nodes = []
    for d in data:
        _id = d["id"]
        children = [_["id"] for _ in data if _id in (_["parents"] or [])]
        nodes.append(Node(id=_id, children=children, parents=d["parents"] or [], fields=d.get("fields") or []))
    return sorted(nodes, key=lambda _: len(_.parents))


def get_model_tree(data: list[dict]) -> list[Node]:
    nodes = sorted(get_model_nodes(data), key=lambda _: len(_.parents))
    tree = []
    while nodes:
        n = nodes.pop(0)
        tree.append(n)
        for c in n.children:
            try:
                tree.index(c)
            except ValueError:
                c = nodes[nodes.index(c)]
            if c not in tree and all(_ in tree for _ in c.parents):
                print(f"adding {c.id}")
                tree.append(nodes.pop(nodes.index(c)))
        nodes = sorted(nodes, key=lambda _: len(_.parents))
    return tree
