# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.597656
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .music_album_production_type import MusicAlbumProductionType
from .music_album_release_type import MusicAlbumReleaseType
from .music_group import MusicGroup
from .music_playlist import MusicPlaylist
from .music_release import MusicRelease
from .person import Person


@dataclass
class MusicAlbum(MusicPlaylist):
    albumProductionType: MusicAlbumProductionType | None
    albumRelease: MusicRelease | None
    albumReleaseType: MusicAlbumReleaseType | None
    byArtist: MusicGroup | Person | None
