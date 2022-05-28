# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.587113
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.drug import Drug
from models.medical_condition import MedicalCondition
from models.medical_device import MedicalDevice
from models.medical_entity import MedicalEntity
from models.medical_enumeration import MedicalEnumeration
from models.medical_sign import MedicalSign
from models.text import Text


@dataclass
class MedicalTest(MedicalEntity):
    affectedBy: Drug | None
    normalRange: MedicalEnumeration | Text | None
    signDetected: MedicalSign | None
    usedToDiagnose: MedicalCondition | None
    usesDevice: MedicalDevice | None
