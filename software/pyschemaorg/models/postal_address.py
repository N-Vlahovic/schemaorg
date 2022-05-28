# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578633
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.contact_point import ContactPoint
from models.country import Country
from models.text import Text


@dataclass
class PostalAddress(ContactPoint):
    addressCountry: Country | Text | None
    addressLocality: Text | None
    addressRegion: Text | None
    postOfficeBoxNumber: Text | None
    postalCode: Text | None
    streetAddress: Text | None
