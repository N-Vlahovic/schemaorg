# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573923
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.medical_specialty import MedicalSpecialty
from models.organization import Organization
from models.text import Text


@dataclass
class MedicalOrganization(Organization):
    healthPlanNetworkId: Text | None
    isAcceptingNewPatients: Boolean | None
    medicalSpecialty: MedicalSpecialty | None
