# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575695
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.alignment_object import AlignmentObject
from models.creative_work import CreativeWork
from models.defined_term import DefinedTerm
from models.text import Text
from models.url import URL


@dataclass
class LearningResource(CreativeWork):
    assesses: DefinedTerm | Text | None
    competencyRequired: DefinedTerm | Text | URL | None
    educationalAlignment: AlignmentObject | None
    educationalLevel: DefinedTerm | Text | URL | None
    educationalUse: DefinedTerm | Text | None
    learningResourceType: DefinedTerm | Text | None
    teaches: DefinedTerm | Text | None
