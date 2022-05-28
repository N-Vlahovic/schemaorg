# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574564
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.medical_intangible import MedicalIntangible
from models.number import Number
from models.qualitative_value import QualitativeValue
from models.text import Text


@dataclass
class DoseSchedule(MedicalIntangible):
    doseUnit: Text | None
    doseValue: Number | QualitativeValue | None
    frequency: Text | None
    targetPopulation: Text | None
