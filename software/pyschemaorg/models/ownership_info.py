# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579860
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date_time import DateTime
from models.organization import Organization
from models.person import Person
from models.product import Product
from models.service import Service
from models.structured_value import StructuredValue


@dataclass
class OwnershipInfo(StructuredValue):
    acquiredFrom: Organization | Person | None
    ownedFrom: DateTime | None
    ownedThrough: DateTime | None
    typeOfGood: Product | Service | None
