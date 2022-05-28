# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579088
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.date_time import DateTime
from models.day_of_week import DayOfWeek
from models.duration import Duration
from models.intangible import Intangible
from models.integer import Integer
from models.text import Text
from models.time import Time


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
