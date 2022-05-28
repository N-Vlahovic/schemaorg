# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.593517
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.anatomical_structure import AnatomicalStructure
from models.anatomical_system import AnatomicalSystem
from models.medical_condition import MedicalCondition
from models.medical_entity import MedicalEntity
from models.medical_therapy import MedicalTherapy
from models.text import Text


@dataclass
class SuperficialAnatomy(MedicalEntity):
    associatedPathophysiology: Text | None
    relatedAnatomy: AnatomicalStructure | AnatomicalSystem | None
    relatedCondition: MedicalCondition | None
    relatedTherapy: MedicalTherapy | None
    significance: Text | None
