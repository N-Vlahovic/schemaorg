# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.588751
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.abstract_base import AbstractBase
from models.enumeration import Enumeration
from models.intangible import Intangible


@dataclass
class Property(Intangible):
    domainIncludes: AbstractBase | None
    inverseOf: Property | None
    rangeIncludes: AbstractBase | None
    supersededBy: Enumeration | Property | None
