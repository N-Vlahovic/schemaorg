# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584507
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.creative_work_season import CreativeWorkSeason
from models.creative_work_series import CreativeWorkSeries
from models.duration import Duration
from models.integer import Integer
from models.music_group import MusicGroup
from models.organization import Organization
from models.person import Person
from models.text import Text
from models.video_object import VideoObject


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
