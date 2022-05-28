# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.593875
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.monetary_amount import MonetaryAmount
from models.number import Number
from models.structured_value import StructuredValue
from models.text import Text
from models.unit_price_specification import UnitPriceSpecification


@dataclass
class ExchangeRateSpecification(StructuredValue):
    currency: Text | None
    currentExchangeRate: UnitPriceSpecification | None
    exchangeRateSpread: MonetaryAmount | Number | None
