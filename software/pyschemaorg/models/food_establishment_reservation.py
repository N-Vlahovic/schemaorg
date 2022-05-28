# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.606249
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date_time import DateTime
from .integer import Integer
from .quantitative_value import QuantitativeValue
from .reservation import Reservation
from .time import Time


@dataclass
class FoodEstablishmentReservation(Reservation):
    endTime: DateTime | Time | None
    partySize: Integer | QuantitativeValue | None
    startTime: DateTime | Time | None
