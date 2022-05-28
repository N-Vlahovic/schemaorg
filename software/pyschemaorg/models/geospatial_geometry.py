# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.600288
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .intangible import Intangible
from .place import Place


@dataclass
class GeospatialGeometry(Intangible):
    geoContains: GeospatialGeometry | Place | None
    geoCoveredBy: GeospatialGeometry | Place | None
    geoCovers: GeospatialGeometry | Place | None
    geoCrosses: GeospatialGeometry | Place | None
    geoDisjoint: GeospatialGeometry | Place | None
    geoEquals: GeospatialGeometry | Place | None
    geoIntersects: GeospatialGeometry | Place | None
    geoOverlaps: GeospatialGeometry | Place | None
    geoTouches: GeospatialGeometry | Place | None
    geoWithin: GeospatialGeometry | Place | None
