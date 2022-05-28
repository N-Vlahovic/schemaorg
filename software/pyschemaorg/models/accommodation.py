# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.579389
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .duration import Duration
from .floor_plan import FloorPlan
from .integer import Integer
from .location_feature_specification import LocationFeatureSpecification
from .number import Number
from .place import Place
from .quantitative_value import QuantitativeValue
from .text import Text
from .url import URL


@dataclass
class Accommodation(Place):
    accommodationCategory: Text | None
    accommodationFloorPlan: FloorPlan | None
    amenityFeature: LocationFeatureSpecification | None
    floorLevel: Text | None
    floorSize: QuantitativeValue | None
    leaseLength: Duration | QuantitativeValue | None
    numberOfBathroomsTotal: Integer | None
    numberOfBedrooms: Number | QuantitativeValue | None
    numberOfFullBathrooms: Number | None
    numberOfPartialBathrooms: Number | None
    numberOfRooms: Number | QuantitativeValue | None
    permittedUsage: Text | None
    petsAllowed: Boolean | Text | None
    tourBookingPage: URL | None
    yearBuilt: Number | None
