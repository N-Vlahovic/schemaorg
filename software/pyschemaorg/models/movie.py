# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585283
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.country import Country
from models.creative_work import CreativeWork
from models.duration import Duration
from models.language import Language
from models.music_group import MusicGroup
from models.organization import Organization
from models.person import Person
from models.text import Text
from models.url import URL
from models.video_object import VideoObject


@dataclass
class Movie(CreativeWork):
    actor: Person | None
    actors: Person | None
    countryOfOrigin: Country | None
    director: Person | None
    directors: Person | None
    duration: Duration | None
    musicBy: MusicGroup | Person | None
    productionCompany: Organization | None
    subtitleLanguage: Language | Text | None
    titleEIDR: Text | URL | None
    trailer: VideoObject | None
