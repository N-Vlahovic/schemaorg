# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.601392
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .monetary_amount import MonetaryAmount
from .number import Number
from .structured_value import StructuredValue


@dataclass
class RepaymentSpecification(StructuredValue):
    downPayment: MonetaryAmount | Number | None
    earlyPrepaymentPenalty: MonetaryAmount | None
    loanPaymentAmount: MonetaryAmount | None
    loanPaymentFrequency: Number | None
    numberOfLoanPayments: Number | None
