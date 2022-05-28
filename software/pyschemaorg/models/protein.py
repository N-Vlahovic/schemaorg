# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.618811
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .bio_chem_entity import BioChemEntity
from .text import Text


@dataclass
class Protein(BioChemEntity):
    hasBioPolymerSequence: Text | None
