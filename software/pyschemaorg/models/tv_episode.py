# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.601253
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .country import Country
from .episode import Episode
from .language import Language
from .tv_series import TVSeries
from .text import Text
from .url import URL


@dataclass
class TVEpisode(Episode):
    countryOfOrigin: Country | None
    partOfTVSeries: TVSeries | None
    subtitleLanguage: Language | Text | None
    titleEIDR: Text | URL | None
