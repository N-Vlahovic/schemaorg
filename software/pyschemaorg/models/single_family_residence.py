# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.590058
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.house import House
from models.number import Number
from models.quantitative_value import QuantitativeValue


@dataclass
class SingleFamilyResidence(House):
    numberOfRooms: Number | QuantitativeValue | None
    occupancy: QuantitativeValue | None
