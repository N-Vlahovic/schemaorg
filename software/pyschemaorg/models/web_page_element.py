# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594067
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.css_selector_type import CssSelectorType
from models.x_path_type import XPathType


@dataclass
class WebPageElement(CreativeWork):
    cssSelector: CssSelectorType | None
    xpath: XPathType | None
