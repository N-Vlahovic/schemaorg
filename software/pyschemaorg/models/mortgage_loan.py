# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584879
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.loan_or_credit import LoanOrCredit
from models.monetary_amount import MonetaryAmount


@dataclass
class MortgageLoan(LoanOrCredit):
    domiciledMortgage: Boolean | None
    loanMortgageMandateAmount: MonetaryAmount | None
