# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.589344
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .duration import Duration
from .how_to import HowTo
from .item_list import ItemList
from .nutrition_information import NutritionInformation
from .quantitative_value import QuantitativeValue
from .restricted_diet import RestrictedDiet
from .text import Text


@dataclass
class Recipe(HowTo):
    cookTime: Duration | None
    cookingMethod: Text | None
    ingredients: Text | None
    nutrition: NutritionInformation | None
    recipeCategory: Text | None
    recipeCuisine: Text | None
    recipeIngredient: Text | None
    recipeInstructions: CreativeWork | ItemList | Text | None
    recipeYield: QuantitativeValue | Text | None
    suitableForDiet: RestrictedDiet | None
