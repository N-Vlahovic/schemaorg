# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594611
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.delivery_method import DeliveryMethod
from models.geo_shape import GeoShape
from models.place import Place
from models.price_specification import PriceSpecification
from models.text import Text


@dataclass
class DeliveryChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: DeliveryMethod | None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None
    eligibleRegion: GeoShape | Place | Text | None
    ineligibleRegion: GeoShape | Place | Text | None
