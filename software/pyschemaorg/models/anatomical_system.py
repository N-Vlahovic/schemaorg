# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.614679
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .anatomical_structure import AnatomicalStructure
from .medical_condition import MedicalCondition
from .medical_entity import MedicalEntity
from .medical_therapy import MedicalTherapy
from .text import Text


@dataclass
class AnatomicalSystem(MedicalEntity):
    associatedPathophysiology: Text | None
    comprisedOf: AnatomicalStructure | AnatomicalSystem | None
    relatedCondition: MedicalCondition | None
    relatedStructure: AnatomicalStructure | None
    relatedTherapy: MedicalTherapy | None
