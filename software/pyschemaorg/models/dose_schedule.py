# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.581959
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .medical_intangible import MedicalIntangible
from .number import Number
from .qualitative_value import QualitativeValue
from .text import Text


@dataclass
class DoseSchedule(MedicalIntangible):
    doseUnit: Text | None
    doseValue: Number | QualitativeValue | None
    frequency: Text | None
    targetPopulation: Text | None
