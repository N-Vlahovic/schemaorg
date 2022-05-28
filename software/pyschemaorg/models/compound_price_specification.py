# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.592197
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .price_specification import PriceSpecification
from .price_type_enumeration import PriceTypeEnumeration
from .text import Text
from .unit_price_specification import UnitPriceSpecification


@dataclass
class CompoundPriceSpecification(PriceSpecification):
    priceComponent: UnitPriceSpecification | None
    priceType: PriceTypeEnumeration | Text | None
