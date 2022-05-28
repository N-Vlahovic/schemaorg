# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585449
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work_series import CreativeWorkSeries
from models.music_group import MusicGroup
from models.organization import Organization
from models.person import Person
from models.video_object import VideoObject


@dataclass
class MovieSeries(CreativeWorkSeries):
    actor: Person | None
    actors: Person | None
    director: Person | None
    directors: Person | None
    musicBy: MusicGroup | Person | None
    productionCompany: Organization | None
    trailer: VideoObject | None
