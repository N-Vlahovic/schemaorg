# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.611038
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .number import Number
from .quantitative_value import QuantitativeValue
from .residence import Residence
from .text import Text
from .url import URL


@dataclass
class ApartmentComplex(Residence):
    numberOfAccommodationUnits: QuantitativeValue | None
    numberOfAvailableAccommodationUnits: QuantitativeValue | None
    numberOfBedrooms: Number | QuantitativeValue | None
    petsAllowed: Boolean | Text | None
    tourBookingPage: URL | None
