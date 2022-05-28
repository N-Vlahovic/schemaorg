# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.592783
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .drug_legal_status import DrugLegalStatus
from .grant import Grant
from .medical_code import MedicalCode
from .medical_enumeration import MedicalEnumeration
from .medical_guideline import MedicalGuideline
from .medical_specialty import MedicalSpecialty
from .medical_study import MedicalStudy
from .medicine_system import MedicineSystem
from .organization import Organization
from .text import Text
from .thing import Thing


@dataclass
class MedicalEntity(Thing):
    code: MedicalCode | None
    funding: Grant | None
    guideline: MedicalGuideline | None
    legalStatus: DrugLegalStatus | MedicalEnumeration | Text | None
    medicineSystem: MedicineSystem | None
    recognizingAuthority: Organization | None
    relevantSpecialty: MedicalSpecialty | None
    study: MedicalStudy | None
