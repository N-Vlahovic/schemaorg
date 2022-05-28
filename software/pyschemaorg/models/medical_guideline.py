# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579187
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.medical_entity import MedicalEntity
from models.medical_evidence_level import MedicalEvidenceLevel
from models.text import Text


@dataclass
class MedicalGuideline(MedicalEntity):
    evidenceLevel: MedicalEvidenceLevel | None
    evidenceOrigin: Text | None
    guidelineDate: Date | None
    guidelineSubject: MedicalEntity | None
