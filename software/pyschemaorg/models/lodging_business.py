# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.590021
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.audience import Audience
from models.boolean import Boolean
from models.date_time import DateTime
from models.language import Language
from models.local_business import LocalBusiness
from models.location_feature_specification import LocationFeatureSpecification
from models.number import Number
from models.quantitative_value import QuantitativeValue
from models.rating import Rating
from models.text import Text
from models.time import Time


@dataclass
class LodgingBusiness(LocalBusiness):
    amenityFeature: LocationFeatureSpecification | None
    audience: Audience | None
    availableLanguage: Language | Text | None
    checkinTime: DateTime | Time | None
    checkoutTime: DateTime | Time | None
    numberOfRooms: Number | QuantitativeValue | None
    petsAllowed: Boolean | Text | None
    starRating: Rating | None
