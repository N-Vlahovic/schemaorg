# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.617272
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .event import Event
from .person import Person
from .text import Text
from .url import URL


@dataclass
class CourseInstance(Event):
    courseMode: Text | URL | None
    courseWorkload: Text | None
    instructor: Person | None
