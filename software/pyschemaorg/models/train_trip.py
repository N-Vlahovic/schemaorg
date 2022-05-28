# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.594157
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .text import Text
from .train_station import TrainStation
from .trip import Trip


@dataclass
class TrainTrip(Trip):
    arrivalPlatform: Text | None
    arrivalStation: TrainStation | None
    departurePlatform: Text | None
    departureStation: TrainStation | None
    trainName: Text | None
    trainNumber: Text | None
