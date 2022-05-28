# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578370
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.bed_details import BedDetails
from models.bed_type import BedType
from models.quantitative_value import QuantitativeValue
from models.room import Room
from models.text import Text


@dataclass
class HotelRoom(Room):
    bed: BedDetails | BedType | Text | None
    occupancy: QuantitativeValue | None
