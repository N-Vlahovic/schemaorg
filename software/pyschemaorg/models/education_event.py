# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.583848
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .defined_term import DefinedTerm
from .event import Event
from .text import Text
from .url import URL


@dataclass
class EducationEvent(Event):
    assesses: DefinedTerm | Text | None
    educationalLevel: DefinedTerm | Text | URL | None
    teaches: DefinedTerm | Text | None
