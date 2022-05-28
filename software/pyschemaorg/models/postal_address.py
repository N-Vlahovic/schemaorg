# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.589911
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .contact_point import ContactPoint
from .country import Country
from .text import Text


@dataclass
class PostalAddress(ContactPoint):
    addressCountry: Country | Text | None
    addressLocality: Text | None
    addressRegion: Text | None
    postOfficeBoxNumber: Text | None
    postalCode: Text | None
    streetAddress: Text | None
