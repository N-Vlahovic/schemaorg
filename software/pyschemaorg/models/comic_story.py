# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.605175
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .person import Person


@dataclass
class ComicStory(CreativeWork):
    artist: Person | None
    colorist: Person | None
    inker: Person | None
    letterer: Person | None
    penciler: Person | None
