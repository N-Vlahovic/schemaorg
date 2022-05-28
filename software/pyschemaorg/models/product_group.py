# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584988
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.defined_term import DefinedTerm
from models.product import Product
from models.text import Text


@dataclass
class ProductGroup(Product):
    hasVariant: Product | None
    productGroupID: Text | None
    variesBy: DefinedTerm | Text | None
