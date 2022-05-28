# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.580954
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.intangible import Intangible
from models.number import Number
from models.organization import Organization
from models.person import Person
from models.quantitative_value import QuantitativeValue
from models.text import Text


@dataclass
class ProgramMembership(Intangible):
    hostingOrganization: Organization | None
    member: Organization | Person | None
    members: Organization | Person | None
    membershipNumber: Text | None
    membershipPointsEarned: Number | QuantitativeValue | None
    programName: Text | None
