# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582353
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .defined_term import DefinedTerm
from .property_value import PropertyValue
from .text import Text
from .thing import Thing
from .url import URL


@dataclass
class Taxon(Thing):
    childTaxon: Taxon | Text | URL | None
    hasDefinedTerm: DefinedTerm | None
    parentTaxon: Taxon | Text | URL | None
    taxonRank: PropertyValue | Text | URL | None
