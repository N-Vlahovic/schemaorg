# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.628175
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .resort import Resort
from .sports_activity_location import SportsActivityLocation


@dataclass
class SkiResort(Resort, SportsActivityLocation):
    pass
