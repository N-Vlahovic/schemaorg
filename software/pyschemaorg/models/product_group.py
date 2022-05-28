# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.600654
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .defined_term import DefinedTerm
from .product import Product
from .text import Text


@dataclass
class ProductGroup(Product):
    hasVariant: Product | None
    productGroupID: Text | None
    variesBy: DefinedTerm | Text | None
