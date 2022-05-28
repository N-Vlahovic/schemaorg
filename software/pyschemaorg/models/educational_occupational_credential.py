# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576327
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.creative_work import CreativeWork
from models.defined_term import DefinedTerm
from models.duration import Duration
from models.organization import Organization
from models.text import Text
from models.url import URL


@dataclass
class EducationalOccupationalCredential(CreativeWork):
    competencyRequired: DefinedTerm | Text | URL | None
    credentialCategory: DefinedTerm | Text | URL | None
    educationalLevel: DefinedTerm | Text | URL | None
    recognizedBy: Organization | None
    validFor: Duration | None
    validIn: AdministrativeArea | None
