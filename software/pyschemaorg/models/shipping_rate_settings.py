# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576711
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.defined_region import DefinedRegion
from models.delivery_charge_specification import DeliveryChargeSpecification
from models.monetary_amount import MonetaryAmount
from models.structured_value import StructuredValue
from models.text import Text


@dataclass
class ShippingRateSettings(StructuredValue):
    doesNotShip: Boolean | None
    freeShippingThreshold: DeliveryChargeSpecification | MonetaryAmount | None
    isUnlabelledFallback: Boolean | None
    shippingDestination: DefinedRegion | None
    shippingLabel: Text | None
    shippingRate: MonetaryAmount | None
