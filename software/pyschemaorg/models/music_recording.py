# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573295
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.duration import Duration
from models.music_album import MusicAlbum
from models.music_composition import MusicComposition
from models.music_group import MusicGroup
from models.music_playlist import MusicPlaylist
from models.person import Person
from models.text import Text


@dataclass
class MusicRecording(CreativeWork):
    byArtist: MusicGroup | Person | None
    duration: Duration | None
    inAlbum: MusicAlbum | None
    inPlaylist: MusicPlaylist | None
    isrcCode: Text | None
    recordingOf: MusicComposition | None
