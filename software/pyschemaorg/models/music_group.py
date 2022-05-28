# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581783
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.item_list import ItemList
from models.music_album import MusicAlbum
from models.music_recording import MusicRecording
from models.performing_group import PerformingGroup
from models.person import Person
from models.text import Text
from models.url import URL


@dataclass
class MusicGroup(PerformingGroup):
    album: MusicAlbum | None
    albums: MusicAlbum | None
    genre: Text | URL | None
    musicGroupMember: Person | None
    track: ItemList | MusicRecording | None
    tracks: MusicRecording | None
