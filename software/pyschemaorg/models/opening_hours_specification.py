# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.599636
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date import Date
from .date_time import DateTime
from .day_of_week import DayOfWeek
from .structured_value import StructuredValue
from .time import Time


@dataclass
class OpeningHoursSpecification(StructuredValue):
    closes: Time | None
    dayOfWeek: DayOfWeek | None
    opens: Time | None
    validFrom: Date | DateTime | None
    validThrough: Date | DateTime | None
