# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.600461
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .loan_or_credit import LoanOrCredit
from .monetary_amount import MonetaryAmount


@dataclass
class MortgageLoan(LoanOrCredit):
    domiciledMortgage: Boolean | None
    loanMortgageMandateAmount: MonetaryAmount | None
