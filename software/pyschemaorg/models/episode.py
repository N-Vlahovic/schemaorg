# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.599764
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .creative_work_season import CreativeWorkSeason
from .creative_work_series import CreativeWorkSeries
from .duration import Duration
from .integer import Integer
from .music_group import MusicGroup
from .organization import Organization
from .person import Person
from .text import Text
from .video_object import VideoObject


@dataclass
class Episode(CreativeWork):
    actor: Person | None
    actors: Person | None
    director: Person | None
    directors: Person | None
    duration: Duration | None
    episodeNumber: Integer | Text | None
    musicBy: MusicGroup | Person | None
    partOfSeason: CreativeWorkSeason | None
    partOfSeries: CreativeWorkSeries | None
    productionCompany: Organization | None
    trailer: VideoObject | None
