# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.602932
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .product import Product
from .product_group import ProductGroup


@dataclass
class ProductModel(Product):
    isVariantOf: ProductGroup | ProductModel | None
    predecessorOf: ProductModel | None
    successorOf: ProductModel | None
