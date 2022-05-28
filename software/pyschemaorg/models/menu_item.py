# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.590215
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.demand import Demand
from models.intangible import Intangible
from models.menu_section import MenuSection
from models.nutrition_information import NutritionInformation
from models.offer import Offer
from models.restricted_diet import RestrictedDiet


@dataclass
class MenuItem(Intangible):
    menuAddOn: MenuItem | MenuSection | None
    nutrition: NutritionInformation | None
    offers: Demand | Offer | None
    suitableForDiet: RestrictedDiet | None
