# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.606320
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .financial_product import FinancialProduct
from .monetary_amount import MonetaryAmount
from .text import Text
from .url import URL


@dataclass
class BankAccount(FinancialProduct):
    accountMinimumInflow: MonetaryAmount | None
    accountOverdraftLimit: MonetaryAmount | None
    bankAccountType: Text | URL | None
