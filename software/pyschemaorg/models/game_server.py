# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579815
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.game_server_status import GameServerStatus
from models.intangible import Intangible
from models.integer import Integer
from models.video_game import VideoGame


@dataclass
class GameServer(Intangible):
    game: VideoGame | None
    playersOnline: Integer | None
    serverStatus: GameServerStatus | None
