# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.626759
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .bio_chem_entity import BioChemEntity
from .defined_term import DefinedTerm
from .text import Text


@dataclass
class ChemicalSubstance(BioChemEntity):
    chemicalComposition: Text | None
    chemicalRole: DefinedTerm | None
    potentialUse: DefinedTerm | None
