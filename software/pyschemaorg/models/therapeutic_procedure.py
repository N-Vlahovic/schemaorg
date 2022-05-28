# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.593544
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .dose_schedule import DoseSchedule
from .drug import Drug
from .medical_entity import MedicalEntity
from .medical_procedure import MedicalProcedure


@dataclass
class TherapeuticProcedure(MedicalProcedure):
    adverseOutcome: MedicalEntity | None
    doseSchedule: DoseSchedule | None
    drug: Drug | None
