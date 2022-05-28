# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.583125
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.date import Date
from models.date_time import DateTime
from models.series import Series
from models.text import Text


@dataclass
class CreativeWorkSeries(CreativeWork, Series):
    endDate: Date | DateTime | None
    issn: Text | None
    startDate: Date | DateTime | None
