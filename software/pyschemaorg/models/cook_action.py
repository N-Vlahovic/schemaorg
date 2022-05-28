# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589426
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.create_action import CreateAction
from models.food_establishment import FoodEstablishment
from models.food_event import FoodEvent
from models.place import Place
from models.recipe import Recipe


@dataclass
class CookAction(CreateAction):
    foodEstablishment: FoodEstablishment | Place | None
    foodEvent: FoodEvent | None
    recipe: Recipe | None
