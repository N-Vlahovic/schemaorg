# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.607410
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .duration import Duration
from .financial_product import FinancialProduct
from .monetary_amount import MonetaryAmount
from .number import Number
from .quantitative_value import QuantitativeValue
from .repayment_specification import RepaymentSpecification
from .text import Text
from .thing import Thing
from .url import URL


@dataclass
class LoanOrCredit(FinancialProduct):
    amount: MonetaryAmount | Number | None
    currency: Text | None
    gracePeriod: Duration | None
    loanRepaymentForm: RepaymentSpecification | None
    loanTerm: QuantitativeValue | None
    loanType: Text | URL | None
    recourseLoan: Boolean | None
    renegotiableLoan: Boolean | None
    requiredCollateral: Text | Thing | None
