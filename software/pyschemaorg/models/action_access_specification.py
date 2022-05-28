# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.587690
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .category_code import CategoryCode
from .date import Date
from .date_time import DateTime
from .geo_shape import GeoShape
from .intangible import Intangible
from .media_subscription import MediaSubscription
from .offer import Offer
from .physical_activity_category import PhysicalActivityCategory
from .place import Place
from .text import Text
from .thing import Thing
from .time import Time
from .url import URL


@dataclass
class ActionAccessSpecification(Intangible):
    availabilityEnds: Date | DateTime | Time | None
    availabilityStarts: Date | DateTime | Time | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    eligibleRegion: GeoShape | Place | Text | None
    expectsAcceptanceOf: Offer | None
    ineligibleRegion: GeoShape | Place | Text | None
    requiresSubscription: Boolean | MediaSubscription | None
