# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.587015
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .aggregate_rating import AggregateRating
from .image_object import ImageObject
from .intangible import Intangible
from .review import Review
from .text import Text
from .url import URL


@dataclass
class Brand(Intangible):
    aggregateRating: AggregateRating | None
    logo: ImageObject | URL | None
    review: Review | None
    slogan: Text | None
