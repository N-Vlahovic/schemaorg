# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.580714
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .medical_specialty import MedicalSpecialty
from .organization import Organization
from .text import Text


@dataclass
class MedicalOrganization(Organization):
    healthPlanNetworkId: Text | None
    isAcceptingNewPatients: Boolean | None
    medicalSpecialty: MedicalSpecialty | None
