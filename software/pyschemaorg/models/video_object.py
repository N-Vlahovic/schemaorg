# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581570
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.image_object import ImageObject
from models.media_object import MediaObject
from models.music_group import MusicGroup
from models.person import Person
from models.text import Text


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
