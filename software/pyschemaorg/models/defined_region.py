# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578513
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.country import Country
from models.postal_code_range_specification import PostalCodeRangeSpecification
from models.structured_value import StructuredValue
from models.text import Text


@dataclass
class DefinedRegion(StructuredValue):
    addressCountry: Country | Text | None
    addressRegion: Text | None
    postalCode: Text | None
    postalCodePrefix: Text | None
    postalCodeRange: PostalCodeRangeSpecification | None
