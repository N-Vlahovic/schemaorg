# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578442
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.maximum_dose_schedule import MaximumDoseSchedule
from models.medical_intangible import MedicalIntangible
from models.number import Number
from models.text import Text


@dataclass
class DrugStrength(MedicalIntangible):
    activeIngredient: Text | None
    availableIn: AdministrativeArea | None
    maximumIntake: MaximumDoseSchedule | None
    strengthUnit: Text | None
    strengthValue: Number | None
