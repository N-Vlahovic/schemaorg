# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579774
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.price_specification import PriceSpecification
from models.price_type_enumeration import PriceTypeEnumeration
from models.text import Text
from models.unit_price_specification import UnitPriceSpecification


@dataclass
class CompoundPriceSpecification(PriceSpecification):
    priceComponent: UnitPriceSpecification | None
    priceType: PriceTypeEnumeration | Text | None
