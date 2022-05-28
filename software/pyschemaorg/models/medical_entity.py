# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.580120
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.drug_legal_status import DrugLegalStatus
from models.grant import Grant
from models.medical_code import MedicalCode
from models.medical_enumeration import MedicalEnumeration
from models.medical_guideline import MedicalGuideline
from models.medical_specialty import MedicalSpecialty
from models.medical_study import MedicalStudy
from models.medicine_system import MedicineSystem
from models.organization import Organization
from models.text import Text
from models.thing import Thing


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
