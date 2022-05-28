# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.597385
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .creative_work_series import CreativeWorkSeries
from .date import Date
from .date_time import DateTime
from .episode import Episode
from .integer import Integer
from .organization import Organization
from .person import Person
from .text import Text
from .video_object import VideoObject


@dataclass
class CreativeWorkSeason(CreativeWork):
    actor: Person | None
    director: Person | None
    endDate: Date | DateTime | None
    episode: Episode | None
    episodes: Episode | None
    numberOfEpisodes: Integer | None
    partOfSeries: CreativeWorkSeries | None
    productionCompany: Organization | None
    seasonNumber: Integer | Text | None
    startDate: Date | DateTime | None
    trailer: VideoObject | None
