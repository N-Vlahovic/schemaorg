# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.608719
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .business_function import BusinessFunction
from .number import Number
from .product import Product
from .service import Service
from .structured_value import StructuredValue
from .text import Text
from .url import URL


@dataclass
class TypeAndQuantityNode(StructuredValue):
    amountOfThisGood: Number | None
    businessFunction: BusinessFunction | None
    typeOfGood: Product | Service | None
    unitCode: Text | URL | None
    unitText: Text | None
