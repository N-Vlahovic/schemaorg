# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.601475
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work_series import CreativeWorkSeries
from .music_group import MusicGroup
from .organization import Organization
from .person import Person
from .video_object import VideoObject


@dataclass
class MovieSeries(CreativeWorkSeries):
    actor: Person | None
    actors: Person | None
    director: Person | None
    directors: Person | None
    musicBy: MusicGroup | Person | None
    productionCompany: Organization | None
    trailer: VideoObject | None
