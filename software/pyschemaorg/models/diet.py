# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.597169
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .lifestyle_modification import LifestyleModification
from .organization import Organization
from .person import Person
from .text import Text


@dataclass
class Diet(CreativeWork, LifestyleModification):
    dietFeatures: Text | None
    endorsers: Organization | Person | None
    expertConsiderations: Text | None
    physiologicalBenefits: Text | None
    risks: Text | None
