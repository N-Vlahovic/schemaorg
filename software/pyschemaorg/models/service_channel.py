# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.594266
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .contact_point import ContactPoint
from .duration import Duration
from .intangible import Intangible
from .language import Language
from .place import Place
from .postal_address import PostalAddress
from .service import Service
from .text import Text
from .url import URL


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
