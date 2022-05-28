# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.595361
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .integer import Integer
from .item_list import ItemList
from .music_recording import MusicRecording


@dataclass
class MusicPlaylist(CreativeWork):
    numTracks: Integer | None
    track: ItemList | MusicRecording | None
    tracks: MusicRecording | None
