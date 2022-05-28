# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.580649
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.dose_schedule import DoseSchedule
from models.drug import Drug
from models.medical_entity import MedicalEntity
from models.medical_procedure import MedicalProcedure


@dataclass
class TherapeuticProcedure(MedicalProcedure):
    adverseOutcome: MedicalEntity | None
    doseSchedule: DoseSchedule | None
    drug: Drug | None
