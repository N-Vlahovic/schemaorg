# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.592674
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.audio_object import AudioObject
from models.book import Book
from models.duration import Duration
from models.person import Person


@dataclass
class Audiobook(AudioObject, Book):
    duration: Duration | None
    readBy: Person | None
