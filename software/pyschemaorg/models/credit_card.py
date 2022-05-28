# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.617158
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .loan_or_credit import LoanOrCredit
from .payment_card import PaymentCard


@dataclass
class CreditCard(LoanOrCredit, PaymentCard):
    pass
