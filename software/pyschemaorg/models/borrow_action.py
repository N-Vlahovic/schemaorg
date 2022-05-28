# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.600294
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.organization import Organization
from models.person import Person
from models.transfer_action import TransferAction


@dataclass
class BorrowAction(TransferAction):
    lender: Organization | Person | None
