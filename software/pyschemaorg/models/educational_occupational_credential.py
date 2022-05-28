# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.585188
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .creative_work import CreativeWork
from .defined_term import DefinedTerm
from .duration import Duration
from .organization import Organization
from .text import Text
from .url import URL


@dataclass
class EducationalOccupationalCredential(CreativeWork):
    competencyRequired: DefinedTerm | Text | URL | None
    credentialCategory: DefinedTerm | Text | URL | None
    educationalLevel: DefinedTerm | Text | URL | None
    recognizedBy: Organization | None
    validFor: Duration | None
    validIn: AdministrativeArea | None
