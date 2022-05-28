# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589765
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.business_function import BusinessFunction
from models.number import Number
from models.product import Product
from models.service import Service
from models.structured_value import StructuredValue
from models.text import Text
from models.url import URL


@dataclass
class TypeAndQuantityNode(StructuredValue):
    amountOfThisGood: Number | None
    businessFunction: BusinessFunction | None
    typeOfGood: Product | Service | None
    unitCode: Text | URL | None
    unitText: Text | None
