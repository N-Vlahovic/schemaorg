# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578681
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date_time import DateTime
from models.integer import Integer
from models.qualitative_value import QualitativeValue
from models.quantitative_value import QuantitativeValue
from models.reservation import Reservation
from models.text import Text
from models.time import Time


@dataclass
class LodgingReservation(Reservation):
    checkinTime: DateTime | Time | None
    checkoutTime: DateTime | Time | None
    lodgingUnitDescription: Text | None
    lodgingUnitType: QualitativeValue | Text | None
    numAdults: Integer | QuantitativeValue | None
    numChildren: Integer | QuantitativeValue | None
