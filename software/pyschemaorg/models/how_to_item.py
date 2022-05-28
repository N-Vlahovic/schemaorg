# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.612271
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .list_item import ListItem
from .number import Number
from .quantitative_value import QuantitativeValue
from .text import Text


@dataclass
class HowToItem(ListItem):
    requiredQuantity: Number | QuantitativeValue | Text | None
