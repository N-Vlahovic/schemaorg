# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.599056
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .category_code import CategoryCode
from .creative_work import CreativeWork
from .date import Date
from .legal_force_status import LegalForceStatus
from .organization import Organization
from .person import Person
from .text import Text
from .url import URL


@dataclass
class Legislation(CreativeWork):
    jurisdiction: AdministrativeArea | Text | None
    legislationApplies: Legislation | None
    legislationChanges: Legislation | None
    legislationConsolidates: Legislation | None
    legislationDate: Date | None
    legislationDateVersion: Date | None
    legislationIdentifier: Text | URL | None
    legislationJurisdiction: AdministrativeArea | Text | None
    legislationLegalForce: LegalForceStatus | None
    legislationPassedBy: Organization | Person | None
    legislationResponsible: Organization | Person | None
    legislationTransposes: Legislation | None
    legislationType: CategoryCode | Text | None
