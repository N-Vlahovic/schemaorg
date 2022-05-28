# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577528
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.category_code import CategoryCode
from models.date import Date
from models.date_time import DateTime
from models.geo_shape import GeoShape
from models.intangible import Intangible
from models.media_subscription import MediaSubscription
from models.offer import Offer
from models.physical_activity_category import PhysicalActivityCategory
from models.place import Place
from models.text import Text
from models.thing import Thing
from models.time import Time
from models.url import URL


@dataclass
class ActionAccessSpecification(Intangible):
    availabilityEnds: Date | DateTime | Time | None
    availabilityStarts: Date | DateTime | Time | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    eligibleRegion: GeoShape | Place | Text | None
    expectsAcceptanceOf: Offer | None
    ineligibleRegion: GeoShape | Place | Text | None
    requiresSubscription: Boolean | MediaSubscription | None
