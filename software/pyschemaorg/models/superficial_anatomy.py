# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.614773
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .anatomical_structure import AnatomicalStructure
from .anatomical_system import AnatomicalSystem
from .medical_condition import MedicalCondition
from .medical_entity import MedicalEntity
from .medical_therapy import MedicalTherapy
from .text import Text


@dataclass
class SuperficialAnatomy(MedicalEntity):
    associatedPathophysiology: Text | None
    relatedAnatomy: AnatomicalStructure | AnatomicalSystem | None
    relatedCondition: MedicalCondition | None
    relatedTherapy: MedicalTherapy | None
    significance: Text | None
