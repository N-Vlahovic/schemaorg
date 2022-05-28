# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579446
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.financial_product import FinancialProduct
from models.monetary_amount import MonetaryAmount
from models.number import Number
from models.payment_method import PaymentMethod


@dataclass
class PaymentCard(FinancialProduct, PaymentMethod):
    cashBack: Boolean | Number | None
    contactlessPayment: Boolean | None
    floorLimit: MonetaryAmount | None
    monthlyMinimumRepaymentAmount: MonetaryAmount | Number | None
