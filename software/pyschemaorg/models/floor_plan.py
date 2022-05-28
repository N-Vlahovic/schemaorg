# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585168
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.accommodation import Accommodation
from models.boolean import Boolean
from models.image_object import ImageObject
from models.intangible import Intangible
from models.integer import Integer
from models.location_feature_specification import LocationFeatureSpecification
from models.number import Number
from models.quantitative_value import QuantitativeValue
from models.text import Text
from models.url import URL


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
