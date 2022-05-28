# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.587569
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.date_time import DateTime
from models.opening_hours_specification import OpeningHoursSpecification
from models.property_value import PropertyValue


@dataclass
class LocationFeatureSpecification(PropertyValue):
    hoursAvailable: OpeningHoursSpecification | None
    validFrom: Date | DateTime | None
    validThrough: Date | DateTime | None
