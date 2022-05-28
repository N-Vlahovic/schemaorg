# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.616208
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .organization import Organization
from .service import Service
from .text import Text


@dataclass
class GovernmentService(Service):
    jurisdiction: AdministrativeArea | Text | None
    serviceOperator: Organization | None
