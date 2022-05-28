# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.585962
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .defined_region import DefinedRegion
from .delivery_charge_specification import DeliveryChargeSpecification
from .monetary_amount import MonetaryAmount
from .structured_value import StructuredValue
from .text import Text


@dataclass
class ShippingRateSettings(StructuredValue):
    doesNotShip: Boolean | None
    freeShippingThreshold: DeliveryChargeSpecification | MonetaryAmount | None
    isUnlabelledFallback: Boolean | None
    shippingDestination: DefinedRegion | None
    shippingLabel: Text | None
    shippingRate: MonetaryAmount | None
