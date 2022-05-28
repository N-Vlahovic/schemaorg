# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.616532
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .intangible import Intangible
from .number import Number
from .organization import Organization
from .person import Person
from .text import Text


@dataclass
class Rating(Intangible):
    author: Organization | Person | None
    bestRating: Number | Text | None
    ratingExplanation: Text | None
    ratingValue: Number | Text | None
    reviewAspect: Text | None
    worstRating: Number | Text | None
