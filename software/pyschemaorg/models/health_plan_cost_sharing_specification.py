# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575240
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.intangible import Intangible
from models.number import Number
from models.price_specification import PriceSpecification
from models.text import Text


@dataclass
class HealthPlanCostSharingSpecification(Intangible):
    healthPlanCoinsuranceOption: Text | None
    healthPlanCoinsuranceRate: Number | None
    healthPlanCopay: PriceSpecification | None
    healthPlanCopayOption: Text | None
    healthPlanPharmacyCategory: Text | None
