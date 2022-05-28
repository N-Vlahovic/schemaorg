# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.609182
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .audience import Audience
from .boolean import Boolean
from .date_time import DateTime
from .language import Language
from .local_business import LocalBusiness
from .location_feature_specification import LocationFeatureSpecification
from .number import Number
from .quantitative_value import QuantitativeValue
from .rating import Rating
from .text import Text
from .time import Time


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
