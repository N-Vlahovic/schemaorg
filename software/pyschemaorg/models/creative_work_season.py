# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.583076
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.creative_work_series import CreativeWorkSeries
from models.date import Date
from models.date_time import DateTime
from models.episode import Episode
from models.integer import Integer
from models.organization import Organization
from models.person import Person
from models.text import Text
from models.video_object import VideoObject


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
