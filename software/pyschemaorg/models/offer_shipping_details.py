# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.585864
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .defined_region import DefinedRegion
from .monetary_amount import MonetaryAmount
from .shipping_delivery_time import ShippingDeliveryTime
from .structured_value import StructuredValue
from .text import Text
from .url import URL


@dataclass
class OfferShippingDetails(StructuredValue):
    deliveryTime: ShippingDeliveryTime | None
    doesNotShip: Boolean | None
    shippingDestination: DefinedRegion | None
    shippingLabel: Text | None
    shippingRate: MonetaryAmount | None
    shippingSettingsLink: URL | None
    transitTimeLabel: Text | None
