# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.597465
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .date import Date
from .date_time import DateTime
from .series import Series
from .text import Text


@dataclass
class CreativeWorkSeries(CreativeWork, Series):
    endDate: Date | DateTime | None
    issn: Text | None
    startDate: Date | DateTime | None
