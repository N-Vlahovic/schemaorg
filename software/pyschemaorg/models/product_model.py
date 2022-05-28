# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.586262
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.product import Product
from models.product_group import ProductGroup


@dataclass
class ProductModel(Product):
    isVariantOf: ProductGroup | ProductModel | None
    predecessorOf: ProductModel | None
    successorOf: ProductModel | None
