# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.591788
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .financial_product import FinancialProduct
from .monetary_amount import MonetaryAmount
from .number import Number
from .payment_method import PaymentMethod


@dataclass
class PaymentCard(FinancialProduct, PaymentMethod):
    cashBack: Boolean | Number | None
    contactlessPayment: Boolean | None
    floorLimit: MonetaryAmount | None
    monthlyMinimumRepaymentAmount: MonetaryAmount | Number | None
