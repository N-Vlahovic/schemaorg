# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.586932
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .computer_language import ComputerLanguage
from .creative_work import CreativeWork
from .software_application import SoftwareApplication
from .text import Text
from .url import URL


@dataclass
class SoftwareSourceCode(CreativeWork):
    codeRepository: URL | None
    codeSampleType: Text | None
    programmingLanguage: ComputerLanguage | Text | None
    runtime: Text | None
    runtimePlatform: Text | None
    sampleType: Text | None
    targetProduct: SoftwareApplication | None
