# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577042
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.airport import Airport
from models.boarding_policy_type import BoardingPolicyType
from models.date_time import DateTime
from models.distance import Distance
from models.duration import Duration
from models.organization import Organization
from models.person import Person
from models.text import Text
from models.trip import Trip
from models.vehicle import Vehicle


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
