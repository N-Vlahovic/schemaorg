# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574027
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.cdcpmd_record import CDCPMDRecord
from models.civic_structure import CivicStructure
from models.dataset import Dataset
from models.emergency_service import EmergencyService
from models.medical_organization import MedicalOrganization
from models.medical_procedure import MedicalProcedure
from models.medical_specialty import MedicalSpecialty
from models.medical_test import MedicalTest
from models.medical_therapy import MedicalTherapy


@dataclass
class Hospital(CivicStructure, EmergencyService, MedicalOrganization):
    availableService: MedicalProcedure | MedicalTest | MedicalTherapy | None
    healthcareReportingData: CDCPMDRecord | Dataset | None
    medicalSpecialty: MedicalSpecialty | None
