# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.583338
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .duration import Duration
from .number import Number
from .structured_value import StructuredValue


@dataclass
class QuantitativeValueDistribution(StructuredValue):
    duration: Duration | None
    median: Number | None
    percentile10: Number | None
    percentile25: Number | None
    percentile75: Number | None
    percentile90: Number | None
