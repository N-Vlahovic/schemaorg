# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578328
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.duration import Duration
from models.how_to import HowTo
from models.item_list import ItemList
from models.nutrition_information import NutritionInformation
from models.quantitative_value import QuantitativeValue
from models.restricted_diet import RestrictedDiet
from models.text import Text


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
