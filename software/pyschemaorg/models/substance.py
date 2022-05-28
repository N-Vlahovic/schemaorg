# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594030
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.maximum_dose_schedule import MaximumDoseSchedule
from models.medical_entity import MedicalEntity
from models.text import Text


@dataclass
class Substance(MedicalEntity):
    activeIngredient: Text | None
    maximumIntake: MaximumDoseSchedule | None
