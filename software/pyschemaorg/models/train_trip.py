# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581044
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.text import Text
from models.train_station import TrainStation
from models.trip import Trip


@dataclass
class TrainTrip(Trip):
    arrivalPlatform: Text | None
    arrivalStation: TrainStation | None
    departurePlatform: Text | None
    departureStation: TrainStation | None
    trainName: Text | None
    trainNumber: Text | None
