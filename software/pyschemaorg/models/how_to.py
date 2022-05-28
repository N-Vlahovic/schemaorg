# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577397
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.duration import Duration
from models.how_to_section import HowToSection
from models.how_to_step import HowToStep
from models.how_to_supply import HowToSupply
from models.how_to_tool import HowToTool
from models.item_list import ItemList
from models.monetary_amount import MonetaryAmount
from models.quantitative_value import QuantitativeValue
from models.text import Text


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
