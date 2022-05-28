# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575051
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.opening_hours_specification import OpeningHoursSpecification
from models.quantitative_value import QuantitativeValue
from models.structured_value import StructuredValue
from models.time import Time


@dataclass
class ShippingDeliveryTime(StructuredValue):
    businessDays: OpeningHoursSpecification | None
    cutoffTime: Time | None
    handlingTime: QuantitativeValue | None
    transitTime: QuantitativeValue | None
