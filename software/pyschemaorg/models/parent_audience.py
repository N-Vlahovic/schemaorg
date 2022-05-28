# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.609757
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .number import Number
from .people_audience import PeopleAudience


@dataclass
class ParentAudience(PeopleAudience):
    childMaxAge: Number | None
    childMinAge: Number | None
