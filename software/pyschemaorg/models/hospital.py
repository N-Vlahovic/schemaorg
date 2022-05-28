# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.580915
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .cdcpmd_record import CDCPMDRecord
from .civic_structure import CivicStructure
from .dataset import Dataset
from .emergency_service import EmergencyService
from .medical_organization import MedicalOrganization
from .medical_procedure import MedicalProcedure
from .medical_specialty import MedicalSpecialty
from .medical_test import MedicalTest
from .medical_therapy import MedicalTherapy


@dataclass
class Hospital(CivicStructure, EmergencyService, MedicalOrganization):
    availableService: MedicalProcedure | MedicalTest | MedicalTherapy | None
    healthcareReportingData: CDCPMDRecord | Dataset | None
    medicalSpecialty: MedicalSpecialty | None
