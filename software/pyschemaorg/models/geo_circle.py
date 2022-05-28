# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585651
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.distance import Distance
from models.geo_coordinates import GeoCoordinates
from models.geo_shape import GeoShape
from models.number import Number
from models.text import Text


@dataclass
class GeoCircle(GeoShape):
    geoMidpoint: GeoCoordinates | None
    geoRadius: Distance | Number | Text | None
