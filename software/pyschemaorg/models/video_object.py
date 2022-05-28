# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.594926
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .image_object import ImageObject
from .media_object import MediaObject
from .music_group import MusicGroup
from .person import Person
from .text import Text


@dataclass
class VideoObject(MediaObject):
    actor: Person | None
    actors: Person | None
    caption: MediaObject | Text | None
    director: Person | None
    directors: Person | None
    embeddedTextCaption: Text | None
    musicBy: MusicGroup | Person | None
    thumbnail: ImageObject | None
    transcript: Text | None
    videoFrameSize: Text | None
    videoQuality: Text | None
