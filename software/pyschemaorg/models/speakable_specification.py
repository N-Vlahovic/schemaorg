# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579965
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.css_selector_type import CssSelectorType
from models.intangible import Intangible
from models.x_path_type import XPathType


@dataclass
class SpeakableSpecification(Intangible):
    cssSelector: CssSelectorType | None
    xpath: XPathType | None
