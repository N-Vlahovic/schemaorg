# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.585311
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work_season import CreativeWorkSeason
from .creative_work_series import CreativeWorkSeries
from .episode import Episode
from .integer import Integer
from .music_group import MusicGroup
from .organization import Organization
from .person import Person
from .url import URL
from .video_object import VideoObject


@dataclass
class RadioSeries(CreativeWorkSeries):
    actor: Person | None
    actors: Person | None
    containsSeason: CreativeWorkSeason | None
    director: Person | None
    directors: Person | None
    episode: Episode | None
    episodes: Episode | None
    musicBy: MusicGroup | Person | None
    numberOfEpisodes: Integer | None
    numberOfSeasons: Integer | None
    productionCompany: Organization | None
    season: CreativeWorkSeason | URL | None
    seasons: CreativeWorkSeason | None
    trailer: VideoObject | None
