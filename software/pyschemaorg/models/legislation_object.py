# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.589134
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .legal_value_level import LegalValueLevel
from .legislation import Legislation
from .media_object import MediaObject


@dataclass
class LegislationObject(Legislation, MediaObject):
    legislationLegalValue: LegalValueLevel | None
