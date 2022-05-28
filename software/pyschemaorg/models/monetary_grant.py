# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.615598
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .grant import Grant
from .monetary_amount import MonetaryAmount
from .number import Number
from .organization import Organization
from .person import Person


@dataclass
class MonetaryGrant(Grant):
    amount: MonetaryAmount | Number | None
    funder: Organization | Person | None
