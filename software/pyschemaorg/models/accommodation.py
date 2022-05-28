# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573202
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.duration import Duration
from models.floor_plan import FloorPlan
from models.integer import Integer
from models.location_feature_specification import LocationFeatureSpecification
from models.number import Number
from models.place import Place
from models.quantitative_value import QuantitativeValue
from models.text import Text
from models.url import URL


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
