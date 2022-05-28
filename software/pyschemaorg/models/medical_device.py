# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.580604
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.medical_contraindication import MedicalContraindication
from models.medical_entity import MedicalEntity
from models.text import Text


@dataclass
class MedicalDevice(MedicalEntity):
    adverseOutcome: MedicalEntity | None
    contraindication: MedicalContraindication | Text | None
    postOp: Text | None
    preOp: Text | None
    procedure: Text | None
    seriousAdverseOutcome: MedicalEntity | None
