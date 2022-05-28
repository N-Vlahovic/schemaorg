# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.579993
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .organization import Organization
from .place import Place
from .text import Text


@dataclass
class LocalBusiness(Organization, Place):
    branchOf: Organization | None
    currenciesAccepted: Text | None
    openingHours: Text | None
    paymentAccepted: Text | None
    priceRange: Text | None
