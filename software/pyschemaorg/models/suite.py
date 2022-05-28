# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.590102
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.accommodation import Accommodation
from models.bed_details import BedDetails
from models.bed_type import BedType
from models.number import Number
from models.quantitative_value import QuantitativeValue
from models.text import Text


@dataclass
class Suite(Accommodation):
    bed: BedDetails | BedType | Text | None
    numberOfRooms: Number | QuantitativeValue | None
    occupancy: QuantitativeValue | None
