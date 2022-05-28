# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.587314
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.game import Game
from models.game_play_mode import GamePlayMode
from models.game_server import GameServer
from models.music_group import MusicGroup
from models.person import Person
from models.software_application import SoftwareApplication
from models.text import Text
from models.thing import Thing
from models.url import URL
from models.video_object import VideoObject


@dataclass
class VideoGame(Game, SoftwareApplication):
    actor: Person | None
    actors: Person | None
    cheatCode: CreativeWork | None
    director: Person | None
    directors: Person | None
    gameEdition: Text | None
    gamePlatform: Text | Thing | URL | None
    gameServer: GameServer | None
    gameTip: CreativeWork | None
    musicBy: MusicGroup | Person | None
    playMode: GamePlayMode | None
    trailer: VideoObject | None
