# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574598
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.qualitative_value import QualitativeValue
from models.reservation import Reservation
from models.text import Text


@dataclass
class FlightReservation(Reservation):
    boardingGroup: Text | None
    passengerPriorityStatus: QualitativeValue | Text | None
    passengerSequenceNumber: Text | None
    securityScreening: Text | None
