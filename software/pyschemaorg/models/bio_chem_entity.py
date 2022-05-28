# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.588083
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.defined_term import DefinedTerm
from models.gene import Gene
from models.grant import Grant
from models.medical_condition import MedicalCondition
from models.property_value import PropertyValue
from models.taxon import Taxon
from models.text import Text
from models.thing import Thing
from models.url import URL


@dataclass
class BioChemEntity(Thing):
    associatedDisease: MedicalCondition | PropertyValue | URL | None
    bioChemInteraction: BioChemEntity | None
    bioChemSimilarity: BioChemEntity | None
    biologicalRole: DefinedTerm | None
    funding: Grant | None
    hasBioChemEntityPart: BioChemEntity | None
    hasMolecularFunction: DefinedTerm | PropertyValue | URL | None
    hasRepresentation: PropertyValue | Text | URL | None
    isEncodedByBioChemEntity: Gene | None
    isInvolvedInBiologicalProcess: DefinedTerm | PropertyValue | URL | None
    isLocatedInSubcellularLocation: DefinedTerm | PropertyValue | URL | None
    isPartOfBioChemEntity: BioChemEntity | None
    taxonomicRange: DefinedTerm | Taxon | Text | URL | None
