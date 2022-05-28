# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594537
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.organization import Organization
from models.person import Person
from models.real_estate_agent import RealEstateAgent
from models.trade_action import TradeAction


@dataclass
class RentAction(TradeAction):
    landlord: Organization | Person | None
    realEstateAgent: RealEstateAgent | None
