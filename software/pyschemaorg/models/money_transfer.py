# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577264
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.bank_or_credit_union import BankOrCreditUnion
from models.monetary_amount import MonetaryAmount
from models.number import Number
from models.text import Text
from models.transfer_action import TransferAction


@dataclass
class MoneyTransfer(TransferAction):
    amount: MonetaryAmount | Number | None
    beneficiaryBank: BankOrCreditUnion | Text | None
