# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.601678
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date_time import DateTime
from .demand import Demand
from .intangible import Intangible
from .item_list import ItemList
from .offer import Offer
from .organization import Organization
from .person import Person
from .place import Place
from .time import Time


@dataclass
class Trip(Intangible):
    arrivalTime: DateTime | Time | None
    departureTime: DateTime | Time | None
    itinerary: ItemList | Place | None
    offers: Demand | Offer | None
    partOfTrip: Trip | None
    provider: Organization | Person | None
    subTrip: Trip | None
