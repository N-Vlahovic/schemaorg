# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.599778
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.action import Action
from models.number import Number
from models.price_specification import PriceSpecification
from models.text import Text


@dataclass
class TradeAction(Action):
    price: Number | Text | None
    priceCurrency: Text | None
    priceSpecification: PriceSpecification | None
