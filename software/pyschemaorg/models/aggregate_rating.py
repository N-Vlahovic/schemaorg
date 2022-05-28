# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.605552
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .integer import Integer
from .rating import Rating
from .thing import Thing


@dataclass
class AggregateRating(Rating):
    itemReviewed: Thing | None
    ratingCount: Integer | None
    reviewCount: Integer | None
