# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585367
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.country import Country
from models.creative_work import CreativeWork
from models.creative_work_season import CreativeWorkSeason
from models.tv_series import TVSeries


@dataclass
class TVSeason(CreativeWork, CreativeWorkSeason):
    countryOfOrigin: Country | None
    partOfTVSeries: TVSeries | None
