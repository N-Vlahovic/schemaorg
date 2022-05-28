# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582277
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .category_code import CategoryCode
from .date import Date
from .date_time import DateTime
from .duration import Duration
from .intangible import Intangible
from .monetary_amount import MonetaryAmount
from .order import Order
from .organization import Organization
from .payment_method import PaymentMethod
from .payment_status_type import PaymentStatusType
from .person import Person
from .physical_activity_category import PhysicalActivityCategory
from .price_specification import PriceSpecification
from .text import Text
from .thing import Thing
from .url import URL


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
