# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.601172
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .country import Country
from .creative_work import CreativeWork
from .duration import Duration
from .language import Language
from .music_group import MusicGroup
from .organization import Organization
from .person import Person
from .text import Text
from .url import URL
from .video_object import VideoObject


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
