# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.609245
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .house import House
from .number import Number
from .quantitative_value import QuantitativeValue


@dataclass
class SingleFamilyResidence(House):
    numberOfRooms: Number | QuantitativeValue | None
    occupancy: QuantitativeValue | None
