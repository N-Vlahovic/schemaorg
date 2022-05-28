# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.607100
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .collection import Collection
from .product import Product
from .type_and_quantity_node import TypeAndQuantityNode


@dataclass
class ProductCollection(Collection, Product):
    includesObject: TypeAndQuantityNode | None
