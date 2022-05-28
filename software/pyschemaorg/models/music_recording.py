# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.579565
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .duration import Duration
from .music_album import MusicAlbum
from .music_composition import MusicComposition
from .music_group import MusicGroup
from .music_playlist import MusicPlaylist
from .person import Person
from .text import Text


@dataclass
class MusicRecording(CreativeWork):
    byArtist: MusicGroup | Person | None
    duration: Duration | None
    inAlbum: MusicAlbum | None
    inPlaylist: MusicPlaylist | None
    isrcCode: Text | None
    recordingOf: MusicComposition | None
