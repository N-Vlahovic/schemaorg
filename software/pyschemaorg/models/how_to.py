# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.587387
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .duration import Duration
from .how_to_section import HowToSection
from .how_to_step import HowToStep
from .how_to_supply import HowToSupply
from .how_to_tool import HowToTool
from .item_list import ItemList
from .monetary_amount import MonetaryAmount
from .quantitative_value import QuantitativeValue
from .text import Text


@dataclass
class HowTo(CreativeWork):
    estimatedCost: MonetaryAmount | Text | None
    performTime: Duration | None
    prepTime: Duration | None
    step: CreativeWork | HowToSection | HowToStep | Text | None
    steps: CreativeWork | ItemList | Text | None
    supply: HowToSupply | Text | None
    tool: HowToTool | Text | None
    totalTime: Duration | None
    yield: QuantitativeValue | Text | None
