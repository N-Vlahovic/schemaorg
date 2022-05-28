# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.585635
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .creative_work_season import CreativeWorkSeason
from .creative_work_series import CreativeWorkSeries
from .episode import Episode
from .game_play_mode import GamePlayMode
from .integer import Integer
from .music_group import MusicGroup
from .organization import Organization
from .person import Person
from .place import Place
from .postal_address import PostalAddress
from .quantitative_value import QuantitativeValue
from .text import Text
from .thing import Thing
from .url import URL
from .video_object import VideoObject


@dataclass
class VideoGameSeries(CreativeWorkSeries):
    actor: Person | None
    actors: Person | None
    characterAttribute: Thing | None
    cheatCode: CreativeWork | None
    containsSeason: CreativeWorkSeason | None
    director: Person | None
    directors: Person | None
    episode: Episode | None
    episodes: Episode | None
    gameItem: Thing | None
    gameLocation: Place | PostalAddress | URL | None
    gamePlatform: Text | Thing | URL | None
    musicBy: MusicGroup | Person | None
    numberOfEpisodes: Integer | None
    numberOfPlayers: QuantitativeValue | None
    numberOfSeasons: Integer | None
    playMode: GamePlayMode | None
    productionCompany: Organization | None
    quest: Thing | None
    season: CreativeWorkSeason | URL | None
    seasons: CreativeWorkSeason | None
    trailer: VideoObject | None
