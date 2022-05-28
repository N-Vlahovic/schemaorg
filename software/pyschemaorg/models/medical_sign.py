# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.612438
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .medical_sign_or_symptom import MedicalSignOrSymptom
from .medical_test import MedicalTest
from .physical_exam import PhysicalExam


@dataclass
class MedicalSign(MedicalSignOrSymptom):
    identifyingExam: PhysicalExam | None
    identifyingTest: MedicalTest | None
