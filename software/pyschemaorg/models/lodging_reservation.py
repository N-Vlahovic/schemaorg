# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.590011
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date_time import DateTime
from .integer import Integer
from .qualitative_value import QualitativeValue
from .quantitative_value import QuantitativeValue
from .reservation import Reservation
from .text import Text
from .time import Time


@dataclass
class LodgingReservation(Reservation):
    checkinTime: DateTime | Time | None
    checkoutTime: DateTime | Time | None
    lodgingUnitDescription: Text | None
    lodgingUnitType: QualitativeValue | Text | None
    numAdults: Integer | QuantitativeValue | None
    numChildren: Integer | QuantitativeValue | None
