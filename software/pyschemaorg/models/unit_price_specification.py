# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.587408
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.duration import Duration
from models.number import Number
from models.price_component_type_enumeration import PriceComponentTypeEnumeration
from models.price_specification import PriceSpecification
from models.price_type_enumeration import PriceTypeEnumeration
from models.quantitative_value import QuantitativeValue
from models.text import Text
from models.url import URL


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
