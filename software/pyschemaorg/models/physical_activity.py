# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585791
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.anatomical_structure import AnatomicalStructure
from models.anatomical_system import AnatomicalSystem
from models.category_code import CategoryCode
from models.lifestyle_modification import LifestyleModification
from models.physical_activity_category import PhysicalActivityCategory
from models.superficial_anatomy import SuperficialAnatomy
from models.text import Text
from models.thing import Thing
from models.url import URL


@dataclass
class PhysicalActivity(LifestyleModification):
    associatedAnatomy: AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    epidemiology: Text | None
    pathophysiology: Text | None
