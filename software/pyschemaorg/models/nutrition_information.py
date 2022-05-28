# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579588
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.energy import Energy
from models.mass import Mass
from models.structured_value import StructuredValue
from models.text import Text


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
