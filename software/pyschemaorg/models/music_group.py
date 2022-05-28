# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.595287
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .item_list import ItemList
from .music_album import MusicAlbum
from .music_recording import MusicRecording
from .performing_group import PerformingGroup
from .person import Person
from .text import Text
from .url import URL


@dataclass
class MusicGroup(PerformingGroup):
    album: MusicAlbum | None
    albums: MusicAlbum | None
    genre: Text | URL | None
    musicGroupMember: Person | None
    track: ItemList | MusicRecording | None
    tracks: MusicRecording | None
