# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584559
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.distance import Distance
from models.integer import Integer
from models.person import Person
from models.quantitative_value import QuantitativeValue
from models.text import Text
from models.url import URL


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
