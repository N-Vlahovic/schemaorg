# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.603310
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .drug import Drug
from .medical_audience import MedicalAudience
from .medical_condition import MedicalCondition
from .person import Person


@dataclass
class Patient(MedicalAudience, Person):
    diagnosis: MedicalCondition | None
    drug: Drug | None
    healthCondition: MedicalCondition | None
