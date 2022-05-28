# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.600967
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .accommodation import Accommodation
from .boolean import Boolean
from .image_object import ImageObject
from .intangible import Intangible
from .integer import Integer
from .location_feature_specification import LocationFeatureSpecification
from .number import Number
from .quantitative_value import QuantitativeValue
from .text import Text
from .url import URL


@dataclass
class FloorPlan(Intangible):
    amenityFeature: LocationFeatureSpecification | None
    floorSize: QuantitativeValue | None
    isPlanForApartment: Accommodation | None
    layoutImage: ImageObject | URL | None
    numberOfAccommodationUnits: QuantitativeValue | None
    numberOfAvailableAccommodationUnits: QuantitativeValue | None
    numberOfBathroomsTotal: Integer | None
    numberOfBedrooms: Number | QuantitativeValue | None
    numberOfFullBathrooms: Number | None
    numberOfPartialBathrooms: Number | None
    numberOfRooms: Number | QuantitativeValue | None
    petsAllowed: Boolean | Text | None
