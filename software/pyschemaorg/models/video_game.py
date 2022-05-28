# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.604615
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .game import Game
from .game_play_mode import GamePlayMode
from .game_server import GameServer
from .music_group import MusicGroup
from .person import Person
from .software_application import SoftwareApplication
from .text import Text
from .thing import Thing
from .url import URL
from .video_object import VideoObject


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
