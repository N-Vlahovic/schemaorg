# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.624679
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .bus_station import BusStation
from .bus_stop import BusStop
from .text import Text
from .trip import Trip


@dataclass
class BusTrip(Trip):
    arrivalBusStop: BusStation | BusStop | None
    busName: Text | None
    busNumber: Text | None
    departureBusStop: BusStation | BusStop | None
