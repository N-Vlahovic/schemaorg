# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577223
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.aggregate_rating import AggregateRating
from models.image_object import ImageObject
from models.intangible import Intangible
from models.review import Review
from models.text import Text
from models.url import URL


@dataclass
class Brand(Intangible):
    aggregateRating: AggregateRating | None
    logo: ImageObject | URL | None
    review: Review | None
    slogan: Text | None
