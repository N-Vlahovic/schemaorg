# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594808
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.bio_chem_entity import BioChemEntity
from models.defined_term import DefinedTerm
from models.quantitative_value import QuantitativeValue
from models.text import Text


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
