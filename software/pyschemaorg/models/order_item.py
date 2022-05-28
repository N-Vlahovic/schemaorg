# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.593349
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .intangible import Intangible
from .number import Number
from .order_status import OrderStatus
from .parcel_delivery import ParcelDelivery
from .product import Product
from .service import Service
from .text import Text


@dataclass
class OrderItem(Intangible):
    orderDelivery: ParcelDelivery | None
    orderItemNumber: Text | None
    orderItemStatus: OrderStatus | None
    orderQuantity: Number | None
    orderedItem: OrderItem | Product | Service | None
