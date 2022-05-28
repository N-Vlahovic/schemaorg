# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.586651
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .airport import Airport
from .boarding_policy_type import BoardingPolicyType
from .date_time import DateTime
from .distance import Distance
from .duration import Duration
from .organization import Organization
from .person import Person
from .text import Text
from .trip import Trip
from .vehicle import Vehicle


@dataclass
class Flight(Trip):
    aircraft: Text | Vehicle | None
    arrivalAirport: Airport | None
    arrivalGate: Text | None
    arrivalTerminal: Text | None
    boardingPolicy: BoardingPolicyType | None
    carrier: Organization | None
    departureAirport: Airport | None
    departureGate: Text | None
    departureTerminal: Text | None
    estimatedFlightDuration: Duration | Text | None
    flightDistance: Distance | Text | None
    flightNumber: Text | None
    mealService: Text | None
    seller: Organization | Person | None
    webCheckinTime: DateTime | None
