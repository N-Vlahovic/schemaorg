# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.613024
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .intangible import Intangible
from .qualitative_value import QualitativeValue
from .text import Text


@dataclass
class Seat(Intangible):
    seatNumber: Text | None
    seatRow: Text | None
    seatSection: Text | None
    seatingType: QualitativeValue | Text | None
