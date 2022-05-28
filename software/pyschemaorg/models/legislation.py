# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584108
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.category_code import CategoryCode
from models.creative_work import CreativeWork
from models.date import Date
from models.legal_force_status import LegalForceStatus
from models.organization import Organization
from models.person import Person
from models.text import Text
from models.url import URL


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
