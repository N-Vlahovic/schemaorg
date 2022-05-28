# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.588404
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.financial_product import FinancialProduct
from models.monetary_amount import MonetaryAmount
from models.text import Text
from models.url import URL


@dataclass
class BankAccount(FinancialProduct):
    accountMinimumInflow: MonetaryAmount | None
    accountOverdraftLimit: MonetaryAmount | None
    bankAccountType: Text | URL | None
