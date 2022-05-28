# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584447
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.date_time import DateTime
from models.day_of_week import DayOfWeek
from models.structured_value import StructuredValue
from models.time import Time


@dataclass
class OpeningHoursSpecification(StructuredValue):
    closes: Time | None
    dayOfWeek: DayOfWeek | None
    opens: Time | None
    validFrom: Date | DateTime | None
    validThrough: Date | DateTime | None
