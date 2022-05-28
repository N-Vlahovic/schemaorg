# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.587528
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .contact_point_option import ContactPointOption
from .geo_shape import GeoShape
from .language import Language
from .opening_hours_specification import OpeningHoursSpecification
from .place import Place
from .product import Product
from .structured_value import StructuredValue
from .text import Text


@dataclass
class ContactPoint(StructuredValue):
    areaServed: AdministrativeArea | GeoShape | Place | Text | None
    availableLanguage: Language | Text | None
    contactOption: ContactPointOption | None
    contactType: Text | None
    email: Text | None
    faxNumber: Text | None
    hoursAvailable: OpeningHoursSpecification | None
    productSupported: Product | Text | None
    serviceArea: AdministrativeArea | GeoShape | Place | None
    telephone: Text | None
