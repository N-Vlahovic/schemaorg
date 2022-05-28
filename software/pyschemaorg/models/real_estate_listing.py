# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.617451
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date import Date
from .date_time import DateTime
from .duration import Duration
from .quantitative_value import QuantitativeValue
from .web_page import WebPage


@dataclass
class RealEstateListing(WebPage):
    datePosted: Date | DateTime | None
    leaseLength: Duration | QuantitativeValue | None
