# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.601327
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .country import Country
from .creative_work import CreativeWork
from .creative_work_season import CreativeWorkSeason
from .tv_series import TVSeries


@dataclass
class TVSeason(CreativeWork, CreativeWorkSeason):
    countryOfOrigin: Country | None
    partOfTVSeries: TVSeries | None
