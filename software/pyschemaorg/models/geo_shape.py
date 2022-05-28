# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.589849
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .country import Country
from .number import Number
from .postal_address import PostalAddress
from .structured_value import StructuredValue
from .text import Text


@dataclass
class GeoShape(StructuredValue):
    address: PostalAddress | Text | None
    addressCountry: Country | Text | None
    box: Text | None
    circle: Text | None
    elevation: Number | Text | None
    line: Text | None
    polygon: Text | None
    postalCode: Text | None
