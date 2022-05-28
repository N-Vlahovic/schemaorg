# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577457
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.contact_point_option import ContactPointOption
from models.geo_shape import GeoShape
from models.language import Language
from models.opening_hours_specification import OpeningHoursSpecification
from models.place import Place
from models.product import Product
from models.structured_value import StructuredValue
from models.text import Text


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
