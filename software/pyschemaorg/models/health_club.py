# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.596958
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .health_and_beauty_business import HealthAndBeautyBusiness
from .sports_activity_location import SportsActivityLocation


@dataclass
class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    pass
