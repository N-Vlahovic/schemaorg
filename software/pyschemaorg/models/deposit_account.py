# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.622600
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .bank_account import BankAccount
from .investment_or_deposit import InvestmentOrDeposit


@dataclass
class DepositAccount(BankAccount, InvestmentOrDeposit):
    pass
