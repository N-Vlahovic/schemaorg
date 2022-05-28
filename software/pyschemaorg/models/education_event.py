# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575646
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.defined_term import DefinedTerm
from models.event import Event
from models.text import Text
from models.url import URL


@dataclass
class EducationEvent(Event):
    assesses: DefinedTerm | Text | None
    educationalLevel: DefinedTerm | Text | URL | None
    teaches: DefinedTerm | Text | None
