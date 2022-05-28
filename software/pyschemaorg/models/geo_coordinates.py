# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578554
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.country import Country
from models.number import Number
from models.postal_address import PostalAddress
from models.structured_value import StructuredValue
from models.text import Text


@dataclass
class GeoCoordinates(StructuredValue):
    address: PostalAddress | Text | None
    addressCountry: Country | Text | None
    elevation: Number | Text | None
    latitude: Number | Text | None
    longitude: Number | Text | None
    postalCode: Text | None
