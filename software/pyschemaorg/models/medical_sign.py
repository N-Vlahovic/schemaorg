# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.592161
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.medical_sign_or_symptom import MedicalSignOrSymptom
from models.medical_test import MedicalTest
from models.physical_exam import PhysicalExam


@dataclass
class MedicalSign(MedicalSignOrSymptom):
    identifyingExam: PhysicalExam | None
    identifyingTest: MedicalTest | None
