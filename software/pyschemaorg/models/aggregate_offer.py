# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.603673
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .demand import Demand
from .integer import Integer
from .number import Number
from .offer import Offer
from .text import Text


@dataclass
class AggregateOffer(Offer):
    highPrice: Number | Text | None
    lowPrice: Number | Text | None
    offerCount: Integer | None
    offers: Demand | Offer | None
