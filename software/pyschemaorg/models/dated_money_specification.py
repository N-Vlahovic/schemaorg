# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.597555
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date import Date
from .date_time import DateTime
from .monetary_amount import MonetaryAmount
from .number import Number
from .structured_value import StructuredValue
from .text import Text


@dataclass
class DatedMoneySpecification(StructuredValue):
    amount: MonetaryAmount | Number | None
    currency: Text | None
    endDate: Date | DateTime | None
    startDate: Date | DateTime | None
