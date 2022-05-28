# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.586750
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .audience import Audience
from .date import Date
from .date_time import DateTime
from .duration import Duration
from .intangible import Intangible
from .organization import Organization
from .service import Service


@dataclass
class Permit(Intangible):
    issuedBy: Organization | None
    issuedThrough: Service | None
    permitAudience: Audience | None
    validFor: Duration | None
    validFrom: Date | DateTime | None
    validIn: AdministrativeArea | None
    validUntil: Date | None
