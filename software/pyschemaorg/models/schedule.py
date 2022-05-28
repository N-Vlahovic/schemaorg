# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.590852
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date import Date
from .date_time import DateTime
from .day_of_week import DayOfWeek
from .duration import Duration
from .intangible import Intangible
from .integer import Integer
from .text import Text
from .time import Time


@dataclass
class Schedule(Intangible):
    byDay: DayOfWeek | Text | None
    byMonth: Integer | None
    byMonthDay: Integer | None
    byMonthWeek: Integer | None
    duration: Duration | None
    endDate: Date | DateTime | None
    endTime: DateTime | Time | None
    exceptDate: Date | DateTime | None
    repeatCount: Integer | None
    repeatFrequency: Duration | Text | None
    scheduleTimezone: Text | None
    startDate: Date | DateTime | None
    startTime: DateTime | Time | None
