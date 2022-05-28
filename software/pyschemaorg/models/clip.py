# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.594557
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .creative_work_season import CreativeWorkSeason
from .creative_work_series import CreativeWorkSeries
from .episode import Episode
from .hyper_toc_entry import HyperTocEntry
from .integer import Integer
from .music_group import MusicGroup
from .number import Number
from .person import Person
from .text import Text


@dataclass
class Clip(CreativeWork):
    actor: Person | None
    actors: Person | None
    clipNumber: Integer | Text | None
    director: Person | None
    directors: Person | None
    endOffset: HyperTocEntry | Number | None
    musicBy: MusicGroup | Person | None
    partOfEpisode: Episode | None
    partOfSeason: CreativeWorkSeason | None
    partOfSeries: CreativeWorkSeries | None
    startOffset: HyperTocEntry | Number | None
