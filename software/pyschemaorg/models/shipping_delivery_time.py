# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582847
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .opening_hours_specification import OpeningHoursSpecification
from .quantitative_value import QuantitativeValue
from .structured_value import StructuredValue
from .time import Time


@dataclass
class ShippingDeliveryTime(StructuredValue):
    businessDays: OpeningHoursSpecification | None
    cutoffTime: Time | None
    handlingTime: QuantitativeValue | None
    transitTime: QuantitativeValue | None
