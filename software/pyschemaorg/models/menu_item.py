# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.609522
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .demand import Demand
from .intangible import Intangible
from .menu_section import MenuSection
from .nutrition_information import NutritionInformation
from .offer import Offer
from .restricted_diet import RestrictedDiet


@dataclass
class MenuItem(Intangible):
    menuAddOn: MenuItem | MenuSection | None
    nutrition: NutritionInformation | None
    offers: Demand | Offer | None
    suitableForDiet: RestrictedDiet | None
