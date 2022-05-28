# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.609704
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .gender_type import GenderType
from .qualitative_value import QualitativeValue
from .quantitative_value import QuantitativeValue
from .size_group_enumeration import SizeGroupEnumeration
from .size_system_enumeration import SizeSystemEnumeration
from .text import Text


@dataclass
class SizeSpecification(QualitativeValue):
    hasMeasurement: QuantitativeValue | None
    sizeGroup: SizeGroupEnumeration | Text | None
    sizeSystem: SizeSystemEnumeration | Text | None
    suggestedAge: QuantitativeValue | None
    suggestedGender: GenderType | Text | None
    suggestedMeasurement: QuantitativeValue | None
