# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577181
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.computer_language import ComputerLanguage
from models.creative_work import CreativeWork
from models.software_application import SoftwareApplication
from models.text import Text
from models.url import URL


@dataclass
class SoftwareSourceCode(CreativeWork):
    codeRepository: URL | None
    codeSampleType: Text | None
    programmingLanguage: ComputerLanguage | Text | None
    runtime: Text | None
    runtimePlatform: Text | None
    sampleType: Text | None
    targetProduct: SoftwareApplication | None
