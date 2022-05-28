# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.602189
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .category_code import CategoryCode
from .physical_activity_category import PhysicalActivityCategory
from .review import Review
from .text import Text
from .thing import Thing
from .url import URL


@dataclass
class Recommendation(Review):
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
