# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.598508
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .audience import Audience
from .contact_point import ContactPoint
from .organization import Organization
from .person import Person
from .trade_action import TradeAction


@dataclass
class DonateAction(TradeAction):
    recipient: Audience | ContactPoint | Organization | Person | None
