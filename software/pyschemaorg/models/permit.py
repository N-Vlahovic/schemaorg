# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577091
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.audience import Audience
from models.date import Date
from models.date_time import DateTime
from models.duration import Duration
from models.intangible import Intangible
from models.organization import Organization
from models.service import Service


@dataclass
class Permit(Intangible):
    issuedBy: Organization | None
    issuedThrough: Service | None
    permitAudience: Audience | None
    validFor: Duration | None
    validFrom: Date | DateTime | None
    validIn: AdministrativeArea | None
    validUntil: Date | None
