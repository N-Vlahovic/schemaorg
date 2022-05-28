# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.592363
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date_time import DateTime
from .organization import Organization
from .person import Person
from .product import Product
from .service import Service
from .structured_value import StructuredValue


@dataclass
class OwnershipInfo(StructuredValue):
    acquiredFrom: Organization | Person | None
    ownedFrom: DateTime | None
    ownedThrough: DateTime | None
    typeOfGood: Product | Service | None
