# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.615516
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .bio_chem_entity import BioChemEntity
from .creative_work import CreativeWork
from .event import Event
from .intangible import Intangible
from .medical_entity import MedicalEntity
from .organization import Organization
from .person import Person
from .product import Product


@dataclass
class Grant(Intangible):
    fundedItem: BioChemEntity | CreativeWork | Event | MedicalEntity | Organization | Person | Product | None
    funder: Organization | Person | None
    sponsor: Organization | Person | None
