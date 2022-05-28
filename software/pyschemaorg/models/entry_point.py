# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.606576
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .digital_platform_enumeration import DigitalPlatformEnumeration
from .intangible import Intangible
from .software_application import SoftwareApplication
from .text import Text
from .url import URL


@dataclass
class EntryPoint(Intangible):
    actionApplication: SoftwareApplication | None
    actionPlatform: DigitalPlatformEnumeration | Text | URL | None
    application: SoftwareApplication | None
    contentType: Text | None
    encodingType: Text | None
    httpMethod: Text | None
    urlTemplate: Text | None
