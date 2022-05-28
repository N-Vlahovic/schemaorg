# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.600396
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .medical_observational_study_design import MedicalObservationalStudyDesign
from .medical_study import MedicalStudy


@dataclass
class MedicalObservationalStudy(MedicalStudy):
    studyDesign: MedicalObservationalStudyDesign | None
