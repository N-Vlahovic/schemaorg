# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.612683
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date_time import DateTime
from .place import Place
from .reservation import Reservation


@dataclass
class RentalCarReservation(Reservation):
    dropoffLocation: Place | None
    dropoffTime: DateTime | None
    pickupLocation: Place | None
    pickupTime: DateTime | None
