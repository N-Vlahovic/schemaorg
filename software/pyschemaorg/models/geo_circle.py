# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.601850
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .distance import Distance
from .geo_coordinates import GeoCoordinates
from .geo_shape import GeoShape
from .number import Number
from .text import Text


@dataclass
class GeoCircle(GeoShape):
    geoMidpoint: GeoCoordinates | None
    geoRadius: Distance | Number | Text | None
