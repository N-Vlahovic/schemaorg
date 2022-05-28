# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.586161
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date_time import DateTime
from models.integer import Integer
from models.place import Place
from models.quantitative_value import QuantitativeValue
from models.reservation import Reservation


@dataclass
class TaxiReservation(Reservation):
    partySize: Integer | QuantitativeValue | None
    pickupLocation: Place | None
    pickupTime: DateTime | None
