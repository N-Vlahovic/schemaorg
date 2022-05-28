# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.591367
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .audience import Audience
from .gender_type import GenderType
from .integer import Integer
from .medical_condition import MedicalCondition
from .number import Number
from .quantitative_value import QuantitativeValue
from .text import Text


@dataclass
class PeopleAudience(Audience):
    healthCondition: MedicalCondition | None
    requiredGender: Text | None
    requiredMaxAge: Integer | None
    requiredMinAge: Integer | None
    suggestedAge: QuantitativeValue | None
    suggestedGender: GenderType | Text | None
    suggestedMaxAge: Number | None
    suggestedMeasurement: QuantitativeValue | None
    suggestedMinAge: Number | None
