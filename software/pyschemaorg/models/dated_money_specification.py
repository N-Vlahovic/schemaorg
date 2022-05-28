# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.583177
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.date_time import DateTime
from models.monetary_amount import MonetaryAmount
from models.number import Number
from models.structured_value import StructuredValue
from models.text import Text


@dataclass
class DatedMoneySpecification(StructuredValue):
    amount: MonetaryAmount | Number | None
    currency: Text | None
    endDate: Date | DateTime | None
    startDate: Date | DateTime | None
