# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.599864
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .distance import Distance
from .integer import Integer
from .person import Person
from .quantitative_value import QuantitativeValue
from .text import Text
from .url import URL


@dataclass
class VisualArtwork(CreativeWork):
    artEdition: Integer | Text | None
    artMedium: Text | URL | None
    artform: Text | URL | None
    artist: Person | None
    artworkSurface: Text | URL | None
    colorist: Person | None
    depth: Distance | QuantitativeValue | None
    height: Distance | QuantitativeValue | None
    inker: Person | None
    letterer: Person | None
    penciler: Person | None
    surface: Text | URL | None
    width: Distance | QuantitativeValue | None
