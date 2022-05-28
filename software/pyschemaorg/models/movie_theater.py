# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.607804
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .civic_structure import CivicStructure
from .entertainment_business import EntertainmentBusiness
from .number import Number


@dataclass
class MovieTheater(CivicStructure, EntertainmentBusiness):
    screenCount: Number | None
