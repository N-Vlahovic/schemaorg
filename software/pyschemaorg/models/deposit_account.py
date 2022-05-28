# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.597781
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.bank_account import BankAccount
from models.investment_or_deposit import InvestmentOrDeposit


@dataclass
class DepositAccount(BankAccount, InvestmentOrDeposit):
    pass
