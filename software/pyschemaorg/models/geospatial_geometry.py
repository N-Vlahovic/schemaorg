# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584780
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.intangible import Intangible
from models.place import Place


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
