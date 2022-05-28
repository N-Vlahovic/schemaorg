# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582427
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.audience import Audience
from models.contact_point import ContactPoint
from models.organization import Organization
from models.person import Person
from models.trade_action import TradeAction


@dataclass
class TipAction(TradeAction):
    recipient: Audience | ContactPoint | Organization | Person | None
