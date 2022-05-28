# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.588859
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.collection import Collection
from models.product import Product
from models.type_and_quantity_node import TypeAndQuantityNode


@dataclass
class ProductCollection(Collection, Product):
    includesObject: TypeAndQuantityNode | None
