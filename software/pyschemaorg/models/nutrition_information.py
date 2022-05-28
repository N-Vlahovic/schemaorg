# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.591877
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .energy import Energy
from .mass import Mass
from .structured_value import StructuredValue
from .text import Text


@dataclass
class NutritionInformation(StructuredValue):
    calories: Energy | None
    carbohydrateContent: Mass | None
    cholesterolContent: Mass | None
    fatContent: Mass | None
    fiberContent: Mass | None
    proteinContent: Mass | None
    saturatedFatContent: Mass | None
    servingSize: Text | None
    sodiumContent: Mass | None
    sugarContent: Mass | None
    transFatContent: Mass | None
    unsaturatedFatContent: Mass | None
