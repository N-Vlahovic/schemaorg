# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.593470
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .medical_contraindication import MedicalContraindication
from .medical_entity import MedicalEntity
from .text import Text


@dataclass
class MedicalDevice(MedicalEntity):
    adverseOutcome: MedicalEntity | None
    contraindication: MedicalContraindication | Text | None
    postOp: Text | None
    preOp: Text | None
    procedure: Text | None
    seriousAdverseOutcome: MedicalEntity | None
