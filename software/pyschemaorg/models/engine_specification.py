# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.593292
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.qualitative_value import QualitativeValue
from models.quantitative_value import QuantitativeValue
from models.structured_value import StructuredValue
from models.text import Text
from models.url import URL


@dataclass
class EngineSpecification(StructuredValue):
    engineDisplacement: QuantitativeValue | None
    enginePower: QuantitativeValue | None
    engineType: QualitativeValue | Text | URL | None
    fuelType: QualitativeValue | Text | URL | None
    torque: QuantitativeValue | None
