# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.616749
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .delivery_method import DeliveryMethod
from .geo_shape import GeoShape
from .place import Place
from .price_specification import PriceSpecification
from .text import Text


@dataclass
class DeliveryChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: DeliveryMethod | None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None
    eligibleRegion: GeoShape | Place | Text | None
    ineligibleRegion: GeoShape | Place | Text | None
