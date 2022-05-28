# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.583147
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .intangible import Intangible
from .number import Number
from .price_specification import PriceSpecification
from .text import Text


@dataclass
class HealthPlanCostSharingSpecification(Intangible):
    healthPlanCoinsuranceOption: Text | None
    healthPlanCoinsuranceRate: Number | None
    healthPlanCopay: PriceSpecification | None
    healthPlanCopayOption: Text | None
    healthPlanPharmacyCategory: Text | None
