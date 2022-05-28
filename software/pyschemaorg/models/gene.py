# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.592719
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.anatomical_structure import AnatomicalStructure
from models.anatomical_system import AnatomicalSystem
from models.bio_chem_entity import BioChemEntity
from models.defined_term import DefinedTerm
from models.text import Text


@dataclass
class Gene(BioChemEntity):
    alternativeOf: Gene | None
    encodesBioChemEntity: BioChemEntity | None
    expressedIn: AnatomicalStructure | AnatomicalSystem | BioChemEntity | DefinedTerm | None
    hasBioPolymerSequence: Text | None
