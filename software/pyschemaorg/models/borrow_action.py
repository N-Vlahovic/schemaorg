# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.626951
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .organization import Organization
from .person import Person
from .transfer_action import TransferAction


@dataclass
class BorrowAction(TransferAction):
    lender: Organization | Person | None
