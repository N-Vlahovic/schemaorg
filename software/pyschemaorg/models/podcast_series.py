# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.612617
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work_series import CreativeWorkSeries
from .data_feed import DataFeed
from .person import Person
from .url import URL


@dataclass
class PodcastSeries(CreativeWorkSeries):
    actor: Person | None
    webFeed: DataFeed | URL | None
