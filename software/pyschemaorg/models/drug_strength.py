# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.589554
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .maximum_dose_schedule import MaximumDoseSchedule
from .medical_intangible import MedicalIntangible
from .number import Number
from .text import Text


@dataclass
class DrugStrength(MedicalIntangible):
    activeIngredient: Text | None
    availableIn: AdministrativeArea | None
    maximumIntake: MaximumDoseSchedule | None
    strengthUnit: Text | None
    strengthValue: Number | None
