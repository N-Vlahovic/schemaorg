# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.630708
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .medical_study import MedicalStudy
from .medical_trial_design import MedicalTrialDesign


@dataclass
class MedicalTrial(MedicalStudy):
    trialDesign: MedicalTrialDesign | None
