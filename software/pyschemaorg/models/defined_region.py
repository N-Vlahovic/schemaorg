# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.589686
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .country import Country
from .postal_code_range_specification import PostalCodeRangeSpecification
from .structured_value import StructuredValue
from .text import Text


@dataclass
class DefinedRegion(StructuredValue):
    addressCountry: Country | Text | None
    addressRegion: Text | None
    postalCode: Text | None
    postalCodePrefix: Text | None
    postalCodeRange: PostalCodeRangeSpecification | None
