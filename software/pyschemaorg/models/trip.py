# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585552
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date_time import DateTime
from models.demand import Demand
from models.intangible import Intangible
from models.item_list import ItemList
from models.offer import Offer
from models.organization import Organization
from models.person import Person
from models.place import Place
from models.time import Time


@dataclass
class Trip(Intangible):
    arrivalTime: DateTime | Time | None
    departureTime: DateTime | Time | None
    itinerary: ItemList | Place | None
    offers: Demand | Offer | None
    partOfTrip: Trip | None
    provider: Organization | Person | None
    subTrip: Trip | None
