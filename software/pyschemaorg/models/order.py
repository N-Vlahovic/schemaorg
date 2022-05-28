# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.580466
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.date import Date
from models.date_time import DateTime
from models.intangible import Intangible
from models.invoice import Invoice
from models.number import Number
from models.offer import Offer
from models.order_item import OrderItem
from models.order_status import OrderStatus
from models.organization import Organization
from models.parcel_delivery import ParcelDelivery
from models.payment_method import PaymentMethod
from models.person import Person
from models.postal_address import PostalAddress
from models.product import Product
from models.service import Service
from models.text import Text
from models.url import URL


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
