# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.590316
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.gender_type import GenderType
from models.qualitative_value import QualitativeValue
from models.quantitative_value import QuantitativeValue
from models.size_group_enumeration import SizeGroupEnumeration
from models.size_system_enumeration import SizeSystemEnumeration
from models.text import Text


@dataclass
class SizeSpecification(QualitativeValue):
    hasMeasurement: QuantitativeValue | None
    sizeGroup: SizeGroupEnumeration | Text | None
    sizeSystem: SizeSystemEnumeration | Text | None
    suggestedAge: QuantitativeValue | None
    suggestedGender: GenderType | Text | None
    suggestedMeasurement: QuantitativeValue | None
