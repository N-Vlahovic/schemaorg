# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589960
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.accommodation import Accommodation
from models.number import Number
from models.quantitative_value import QuantitativeValue


@dataclass
class House(Accommodation):
    numberOfRooms: Number | QuantitativeValue | None
