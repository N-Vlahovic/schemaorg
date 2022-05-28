# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.608098
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .create_action import CreateAction
from .food_establishment import FoodEstablishment
from .food_event import FoodEvent
from .place import Place
from .recipe import Recipe


@dataclass
class CookAction(CreateAction):
    foodEstablishment: FoodEstablishment | Place | None
    foodEvent: FoodEvent | None
    recipe: Recipe | None
