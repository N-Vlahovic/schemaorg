# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589589
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.date import Date
from models.date_time import DateTime
from models.number import Number
from models.structured_value import StructuredValue
from models.text import Text


@dataclass
class MonetaryAmount(StructuredValue):
    currency: Text | None
    maxValue: Number | None
    minValue: Number | None
    validFrom: Date | DateTime | None
    validThrough: Date | DateTime | None
    value: Boolean | Number | StructuredValue | Text | None
