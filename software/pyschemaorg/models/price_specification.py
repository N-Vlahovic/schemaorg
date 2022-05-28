# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582504
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .date import Date
from .date_time import DateTime
from .number import Number
from .quantitative_value import QuantitativeValue
from .structured_value import StructuredValue
from .text import Text


@dataclass
class PriceSpecification(StructuredValue):
    eligibleQuantity: QuantitativeValue | None
    eligibleTransactionVolume: PriceSpecification | None
    maxPrice: Number | None
    minPrice: Number | None
    price: Number | Text | None
    priceCurrency: Text | None
    validFrom: Date | DateTime | None
    validThrough: Date | DateTime | None
    valueAddedTaxIncluded: Boolean | None
