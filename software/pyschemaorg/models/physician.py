# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585969
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.hospital import Hospital
from models.medical_business import MedicalBusiness
from models.medical_organization import MedicalOrganization
from models.medical_procedure import MedicalProcedure
from models.medical_specialty import MedicalSpecialty
from models.medical_test import MedicalTest
from models.medical_therapy import MedicalTherapy


@dataclass
class Physician(MedicalBusiness, MedicalOrganization):
    availableService: MedicalProcedure | MedicalTest | MedicalTherapy | None
    hospitalAffiliation: Hospital | None
    medicalSpecialty: MedicalSpecialty | None
