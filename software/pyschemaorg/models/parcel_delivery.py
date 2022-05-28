# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.579703
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date import Date
from .date_time import DateTime
from .delivery_event import DeliveryEvent
from .delivery_method import DeliveryMethod
from .intangible import Intangible
from .order import Order
from .organization import Organization
from .person import Person
from .postal_address import PostalAddress
from .product import Product
from .text import Text
from .url import URL


@dataclass
class ParcelDelivery(Intangible):
    carrier: Organization | None
    deliveryAddress: PostalAddress | None
    deliveryStatus: DeliveryEvent | None
    expectedArrivalFrom: Date | DateTime | None
    expectedArrivalUntil: Date | DateTime | None
    hasDeliveryMethod: DeliveryMethod | None
    itemShipped: Product | None
    originAddress: PostalAddress | None
    partOfOrder: Order | None
    provider: Organization | Person | None
    trackingNumber: Text | None
    trackingUrl: URL | None
