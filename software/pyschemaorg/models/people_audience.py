# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579372
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.audience import Audience
from models.gender_type import GenderType
from models.integer import Integer
from models.medical_condition import MedicalCondition
from models.number import Number
from models.quantitative_value import QuantitativeValue
from models.text import Text


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
