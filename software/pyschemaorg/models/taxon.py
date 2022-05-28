# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574771
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.defined_term import DefinedTerm
from models.property_value import PropertyValue
from models.text import Text
from models.thing import Thing
from models.url import URL


@dataclass
class Taxon(Thing):
    childTaxon: Taxon | Text | URL | None
    hasDefinedTerm: DefinedTerm | None
    parentTaxon: Taxon | Text | URL | None
    taxonRank: PropertyValue | Text | URL | None
