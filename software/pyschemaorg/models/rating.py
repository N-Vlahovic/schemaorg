# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594499
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.intangible import Intangible
from models.number import Number
from models.organization import Organization
from models.person import Person
from models.text import Text


@dataclass
class Rating(Intangible):
    author: Organization | Person | None
    bestRating: Number | Text | None
    ratingExplanation: Text | None
    ratingValue: Number | Text | None
    reviewAspect: Text | None
    worstRating: Number | Text | None
