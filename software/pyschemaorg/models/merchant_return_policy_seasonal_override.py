# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574261
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.date_time import DateTime
from models.intangible import Intangible
from models.integer import Integer
from models.merchant_return_enumeration import MerchantReturnEnumeration


@dataclass
class MerchantReturnPolicySeasonalOverride(Intangible):
    endDate: Date | DateTime | None
    merchantReturnDays: Date | DateTime | Integer | None
    returnPolicyCategory: MerchantReturnEnumeration | None
    startDate: Date | DateTime | None
