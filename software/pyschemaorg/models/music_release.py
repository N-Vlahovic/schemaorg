# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.596716
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .duration import Duration
from .music_album import MusicAlbum
from .music_playlist import MusicPlaylist
from .music_release_format_type import MusicReleaseFormatType
from .organization import Organization
from .person import Person
from .text import Text


@dataclass
class MusicRelease(MusicPlaylist):
    catalogNumber: Text | None
    creditedTo: Organization | Person | None
    duration: Duration | None
    musicReleaseFormat: MusicReleaseFormatType | None
    recordLabel: Organization | None
    releaseOf: MusicAlbum | None
