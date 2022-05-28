# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.613314
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .audio_object import AudioObject
from .book import Book
from .duration import Duration
from .person import Person


@dataclass
class Audiobook(AudioObject, Book):
    duration: Duration | None
    readBy: Person | None
