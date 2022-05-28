# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.588823
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.gender_type import GenderType
from models.person import Person
from models.sports_organization import SportsOrganization
from models.text import Text


@dataclass
class SportsTeam(SportsOrganization):
    athlete: Person | None
    coach: Person | None
    gender: GenderType | Text | None
