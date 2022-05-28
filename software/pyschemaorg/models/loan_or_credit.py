# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589023
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.duration import Duration
from models.financial_product import FinancialProduct
from models.monetary_amount import MonetaryAmount
from models.number import Number
from models.quantitative_value import QuantitativeValue
from models.repayment_specification import RepaymentSpecification
from models.text import Text
from models.thing import Thing
from models.url import URL


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
