# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.602425
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .hospital import Hospital
from .medical_business import MedicalBusiness
from .medical_organization import MedicalOrganization
from .medical_procedure import MedicalProcedure
from .medical_specialty import MedicalSpecialty
from .medical_test import MedicalTest
from .medical_therapy import MedicalTherapy


@dataclass
class Physician(MedicalBusiness, MedicalOrganization):
    availableService: MedicalProcedure | MedicalTest | MedicalTherapy | None
    hospitalAffiliation: Hospital | None
    medicalSpecialty: MedicalSpecialty | None
