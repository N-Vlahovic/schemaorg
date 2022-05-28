# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573363
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.date_time import DateTime
from models.delivery_event import DeliveryEvent
from models.delivery_method import DeliveryMethod
from models.intangible import Intangible
from models.order import Order
from models.organization import Organization
from models.person import Person
from models.postal_address import PostalAddress
from models.product import Product
from models.text import Text
from models.url import URL


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
