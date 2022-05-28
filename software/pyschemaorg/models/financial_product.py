# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.580564
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .number import Number
from .quantitative_value import QuantitativeValue
from .service import Service
from .text import Text
from .url import URL


@dataclass
class FinancialProduct(Service):
    annualPercentageRate: Number | QuantitativeValue | None
    feesAndCommissionsSpecification: Text | URL | None
    interestRate: Number | QuantitativeValue | None
