# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582667
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.duration import Duration
from models.music_album import MusicAlbum
from models.music_playlist import MusicPlaylist
from models.music_release_format_type import MusicReleaseFormatType
from models.organization import Organization
from models.person import Person
from models.text import Text


@dataclass
class MusicRelease(MusicPlaylist):
    catalogNumber: Text | None
    creditedTo: Organization | Person | None
    duration: Duration | None
    musicReleaseFormat: MusicReleaseFormatType | None
    recordLabel: Organization | None
    releaseOf: MusicAlbum | None
