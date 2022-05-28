# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.587103
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .bank_or_credit_union import BankOrCreditUnion
from .monetary_amount import MonetaryAmount
from .number import Number
from .text import Text
from .transfer_action import TransferAction


@dataclass
class MoneyTransfer(TransferAction):
    amount: MonetaryAmount | Number | None
    beneficiaryBank: BankOrCreditUnion | Text | None
