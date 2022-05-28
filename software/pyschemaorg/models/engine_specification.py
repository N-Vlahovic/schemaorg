# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.614359
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .qualitative_value import QualitativeValue
from .quantitative_value import QuantitativeValue
from .structured_value import StructuredValue
from .text import Text
from .url import URL


@dataclass
class EngineSpecification(StructuredValue):
    engineDisplacement: QuantitativeValue | None
    enginePower: QuantitativeValue | None
    engineType: QualitativeValue | Text | URL | None
    fuelType: QualitativeValue | Text | URL | None
    torque: QuantitativeValue | None
