# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.617101
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .bio_chem_entity import BioChemEntity
from .defined_term import DefinedTerm
from .quantitative_value import QuantitativeValue
from .text import Text


@dataclass
class MolecularEntity(BioChemEntity):
    chemicalRole: DefinedTerm | None
    inChI: Text | None
    inChIKey: Text | None
    iupacName: Text | None
    molecularFormula: Text | None
    molecularWeight: QuantitativeValue | Text | None
    monoisotopicMolecularWeight: QuantitativeValue | Text | None
    potentialUse: DefinedTerm | None
    smiles: Text | None
