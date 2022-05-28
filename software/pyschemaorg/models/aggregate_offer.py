# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.586735
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.demand import Demand
from models.integer import Integer
from models.number import Number
from models.offer import Offer
from models.text import Text


@dataclass
class AggregateOffer(Offer):
    highPrice: Number | Text | None
    lowPrice: Number | Text | None
    offerCount: Integer | None
    offers: Demand | Offer | None
