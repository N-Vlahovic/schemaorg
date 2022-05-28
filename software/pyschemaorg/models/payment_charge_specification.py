# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.628686
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .delivery_method import DeliveryMethod
from .payment_method import PaymentMethod
from .price_specification import PriceSpecification


@dataclass
class PaymentChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: DeliveryMethod | None
    appliesToPaymentMethod: PaymentMethod | None
