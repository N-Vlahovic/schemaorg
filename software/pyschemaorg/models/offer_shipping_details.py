# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576662
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.defined_region import DefinedRegion
from models.monetary_amount import MonetaryAmount
from models.shipping_delivery_time import ShippingDeliveryTime
from models.structured_value import StructuredValue
from models.text import Text
from models.url import URL


@dataclass
class OfferShippingDetails(StructuredValue):
    deliveryTime: ShippingDeliveryTime | None
    doesNotShip: Boolean | None
    shippingDestination: DefinedRegion | None
    shippingLabel: Text | None
    shippingRate: MonetaryAmount | None
    shippingSettingsLink: URL | None
    transitTimeLabel: Text | None
