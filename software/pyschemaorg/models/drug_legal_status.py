# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581693
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.medical_intangible import MedicalIntangible


@dataclass
class DrugLegalStatus(MedicalIntangible):
    applicableLocation: AdministrativeArea | None
