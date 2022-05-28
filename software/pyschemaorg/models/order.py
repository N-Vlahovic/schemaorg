# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.593252
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .date import Date
from .date_time import DateTime
from .intangible import Intangible
from .invoice import Invoice
from .number import Number
from .offer import Offer
from .order_item import OrderItem
from .order_status import OrderStatus
from .organization import Organization
from .parcel_delivery import ParcelDelivery
from .payment_method import PaymentMethod
from .person import Person
from .postal_address import PostalAddress
from .product import Product
from .service import Service
from .text import Text
from .url import URL


@dataclass
class Order(Intangible):
    acceptedOffer: Offer | None
    billingAddress: PostalAddress | None
    broker: Organization | Person | None
    confirmationNumber: Text | None
    customer: Organization | Person | None
    discount: Number | Text | None
    discountCode: Text | None
    discountCurrency: Text | None
    isGift: Boolean | None
    merchant: Organization | Person | None
    orderDate: Date | DateTime | None
    orderDelivery: ParcelDelivery | None
    orderNumber: Text | None
    orderStatus: OrderStatus | None
    orderedItem: OrderItem | Product | Service | None
    partOfInvoice: Invoice | None
    paymentDue: DateTime | None
    paymentDueDate: Date | DateTime | None
    paymentMethod: PaymentMethod | None
    paymentMethodId: Text | None
    paymentUrl: URL | None
    seller: Organization | Person | None
