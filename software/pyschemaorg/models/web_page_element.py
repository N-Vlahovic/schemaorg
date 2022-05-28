# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.615782
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .css_selector_type import CssSelectorType
from .x_path_type import XPathType


@dataclass
class WebPageElement(CreativeWork):
    cssSelector: CssSelectorType | None
    xpath: XPathType | None
