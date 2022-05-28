# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.580526
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.intangible import Intangible
from models.number import Number
from models.order_status import OrderStatus
from models.parcel_delivery import ParcelDelivery
from models.product import Product
from models.service import Service
from models.text import Text


@dataclass
class OrderItem(Intangible):
    orderDelivery: ParcelDelivery | None
    orderItemNumber: Text | None
    orderItemStatus: OrderStatus | None
    orderQuantity: Number | None
    orderedItem: OrderItem | Product | Service | None
