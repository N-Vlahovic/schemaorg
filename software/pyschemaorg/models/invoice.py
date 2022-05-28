# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574729
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.category_code import CategoryCode
from models.date import Date
from models.date_time import DateTime
from models.duration import Duration
from models.intangible import Intangible
from models.monetary_amount import MonetaryAmount
from models.order import Order
from models.organization import Organization
from models.payment_method import PaymentMethod
from models.payment_status_type import PaymentStatusType
from models.person import Person
from models.physical_activity_category import PhysicalActivityCategory
from models.price_specification import PriceSpecification
from models.text import Text
from models.thing import Thing
from models.url import URL


@dataclass
class Invoice(Intangible):
    accountId: Text | None
    billingPeriod: Duration | None
    broker: Organization | Person | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    confirmationNumber: Text | None
    customer: Organization | Person | None
    minimumPaymentDue: MonetaryAmount | PriceSpecification | None
    paymentDue: DateTime | None
    paymentDueDate: Date | DateTime | None
    paymentMethod: PaymentMethod | None
    paymentMethodId: Text | None
    paymentStatus: PaymentStatusType | Text | None
    provider: Organization | Person | None
    referencesOrder: Order | None
    scheduledPaymentDate: Date | None
    totalPaymentDue: MonetaryAmount | PriceSpecification | None
