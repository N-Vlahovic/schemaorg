# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.602103
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .anatomical_structure import AnatomicalStructure
from .anatomical_system import AnatomicalSystem
from .category_code import CategoryCode
from .lifestyle_modification import LifestyleModification
from .physical_activity_category import PhysicalActivityCategory
from .superficial_anatomy import SuperficialAnatomy
from .text import Text
from .thing import Thing
from .url import URL


@dataclass
class PhysicalActivity(LifestyleModification):
    associatedAnatomy: AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    epidemiology: Text | None
    pathophysiology: Text | None
