# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576539
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.creative_work_season import CreativeWorkSeason
from models.creative_work_series import CreativeWorkSeries
from models.episode import Episode
from models.game_play_mode import GamePlayMode
from models.integer import Integer
from models.music_group import MusicGroup
from models.organization import Organization
from models.person import Person
from models.place import Place
from models.postal_address import PostalAddress
from models.quantitative_value import QuantitativeValue
from models.text import Text
from models.thing import Thing
from models.url import URL
from models.video_object import VideoObject


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
