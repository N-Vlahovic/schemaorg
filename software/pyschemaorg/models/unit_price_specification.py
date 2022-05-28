# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.604773
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .duration import Duration
from .number import Number
from .price_component_type_enumeration import PriceComponentTypeEnumeration
from .price_specification import PriceSpecification
from .price_type_enumeration import PriceTypeEnumeration
from .quantitative_value import QuantitativeValue
from .text import Text
from .url import URL


@dataclass
class UnitPriceSpecification(PriceSpecification):
    billingDuration: Duration | Number | QuantitativeValue | None
    billingIncrement: Number | None
    billingStart: Number | None
    priceComponentType: PriceComponentTypeEnumeration | None
    priceType: PriceTypeEnumeration | Text | None
    referenceQuantity: QuantitativeValue | None
    unitCode: Text | URL | None
    unitText: Text | None
