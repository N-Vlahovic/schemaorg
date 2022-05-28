# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.587922
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.integer import Integer
from models.rating import Rating
from models.thing import Thing


@dataclass
class AggregateRating(Rating):
    itemReviewed: Thing | None
    ratingCount: Integer | None
    reviewCount: Integer | None
