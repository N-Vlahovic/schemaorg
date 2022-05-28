# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581119
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.contact_point import ContactPoint
from models.duration import Duration
from models.intangible import Intangible
from models.language import Language
from models.place import Place
from models.postal_address import PostalAddress
from models.service import Service
from models.text import Text
from models.url import URL


@dataclass
class ServiceChannel(Intangible):
    availableLanguage: Language | Text | None
    processingTime: Duration | None
    providesService: Service | None
    serviceLocation: Place | None
    servicePhone: ContactPoint | None
    servicePostalAddress: PostalAddress | None
    serviceSmsNumber: ContactPoint | None
    serviceUrl: URL | None
