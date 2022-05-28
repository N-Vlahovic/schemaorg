# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575366
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.duration import Duration
from models.number import Number
from models.structured_value import StructuredValue


@dataclass
class QuantitativeValueDistribution(StructuredValue):
    duration: Duration | None
    median: Number | None
    percentile10: Number | None
    percentile25: Number | None
    percentile75: Number | None
    percentile90: Number | None
