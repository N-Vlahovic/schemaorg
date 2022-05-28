# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.593191
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.medical_contraindication import MedicalContraindication
from models.medical_entity import MedicalEntity
from models.text import Text
from models.therapeutic_procedure import TherapeuticProcedure


@dataclass
class MedicalTherapy(TherapeuticProcedure):
    contraindication: MedicalContraindication | Text | None
    duplicateTherapy: MedicalTherapy | None
    seriousAdverseOutcome: MedicalEntity | None
