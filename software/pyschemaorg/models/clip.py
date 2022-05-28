# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581341
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.creative_work_season import CreativeWorkSeason
from models.creative_work_series import CreativeWorkSeries
from models.episode import Episode
from models.hyper_toc_entry import HyperTocEntry
from models.integer import Integer
from models.music_group import MusicGroup
from models.number import Number
from models.person import Person
from models.text import Text


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
