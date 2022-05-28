# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.633188
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .medical_condition import MedicalCondition
from .medical_therapy import MedicalTherapy


@dataclass
class MedicalSignOrSymptom(MedicalCondition):
    possibleTreatment: MedicalTherapy | None
