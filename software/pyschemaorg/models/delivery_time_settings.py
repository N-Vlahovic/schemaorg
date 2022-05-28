# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.585763
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .defined_region import DefinedRegion
from .shipping_delivery_time import ShippingDeliveryTime
from .structured_value import StructuredValue
from .text import Text


@dataclass
class DeliveryTimeSettings(StructuredValue):
    deliveryTime: ShippingDeliveryTime | None
    isUnlabelledFallback: Boolean | None
    shippingDestination: DefinedRegion | None
    transitTimeLabel: Text | None
