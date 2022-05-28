# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594904
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.event import Event
from models.person import Person
from models.text import Text
from models.url import URL


@dataclass
class CourseInstance(Event):
    courseMode: Text | URL | None
    courseWorkload: Text | None
    instructor: Person | None
