# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582020
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .qualitative_value import QualitativeValue
from .reservation import Reservation
from .text import Text


@dataclass
class FlightReservation(Reservation):
    boardingGroup: Text | None
    passengerPriorityStatus: QualitativeValue | Text | None
    passengerSequenceNumber: Text | None
    securityScreening: Text | None
