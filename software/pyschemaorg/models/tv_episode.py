# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585328
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.country import Country
from models.episode import Episode
from models.language import Language
from models.tv_series import TVSeries
from models.text import Text
from models.url import URL


@dataclass
class TVEpisode(Episode):
    countryOfOrigin: Country | None
    partOfTVSeries: TVSeries | None
    subtitleLanguage: Language | Text | None
    titleEIDR: Text | URL | None
