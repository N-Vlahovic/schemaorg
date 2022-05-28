# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.604285
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .drug import Drug
from .medical_condition import MedicalCondition
from .medical_device import MedicalDevice
from .medical_entity import MedicalEntity
from .medical_enumeration import MedicalEnumeration
from .medical_sign import MedicalSign
from .text import Text


@dataclass
class MedicalTest(MedicalEntity):
    affectedBy: Drug | None
    normalRange: MedicalEnumeration | Text | None
    signDetected: MedicalSign | None
    usedToDiagnose: MedicalCondition | None
    usesDevice: MedicalDevice | None
