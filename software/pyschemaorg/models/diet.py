# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582945
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.lifestyle_modification import LifestyleModification
from models.organization import Organization
from models.person import Person
from models.text import Text


@dataclass
class Diet(CreativeWork, LifestyleModification):
    dietFeatures: Text | None
    endorsers: Organization | Person | None
    expertConsiderations: Text | None
    physiologicalBenefits: Text | None
    risks: Text | None
