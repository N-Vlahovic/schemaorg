# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.581455
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .organization import Organization
from .person import Person
from .trade_action import TradeAction
from .warranty_promise import WarrantyPromise


@dataclass
class BuyAction(TradeAction):
    seller: Organization | Person | None
    vendor: Organization | Person | None
    warrantyPromise: WarrantyPromise | None
