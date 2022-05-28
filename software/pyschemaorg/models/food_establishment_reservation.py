# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.588365
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date_time import DateTime
from models.integer import Integer
from models.quantitative_value import QuantitativeValue
from models.reservation import Reservation
from models.time import Time


@dataclass
class FoodEstablishmentReservation(Reservation):
    endTime: DateTime | Time | None
    partySize: Integer | QuantitativeValue | None
    startTime: DateTime | Time | None
