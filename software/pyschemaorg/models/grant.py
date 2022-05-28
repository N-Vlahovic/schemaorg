# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.593925
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.bio_chem_entity import BioChemEntity
from models.creative_work import CreativeWork
from models.event import Event
from models.intangible import Intangible
from models.medical_entity import MedicalEntity
from models.organization import Organization
from models.person import Person
from models.product import Product


@dataclass
class Grant(Intangible):
    fundedItem: BioChemEntity | CreativeWork | Event | MedicalEntity | Organization | Person | Product | None
    funder: Organization | Person | None
    sponsor: Organization | Person | None
