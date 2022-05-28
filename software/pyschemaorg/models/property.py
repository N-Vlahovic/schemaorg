# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.606909
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .class import Class
from .enumeration import Enumeration
from .intangible import Intangible


@dataclass
class Property(Intangible):
    domainIncludes: Class | None
    inverseOf: Property | None
    rangeIncludes: Class | None
    supersededBy: Class | Enumeration | Property | None
