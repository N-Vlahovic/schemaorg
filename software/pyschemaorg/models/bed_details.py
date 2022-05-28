# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.608891
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .bed_type import BedType
from .intangible import Intangible
from .number import Number
from .text import Text


@dataclass
class BedDetails(Intangible):
    numberOfBeds: Number | None
    typeOfBed: BedType | Text | None
