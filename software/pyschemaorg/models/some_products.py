# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.598963
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.product import Product
from models.quantitative_value import QuantitativeValue


@dataclass
class SomeProducts(Product):
    inventoryLevel: QuantitativeValue | None
