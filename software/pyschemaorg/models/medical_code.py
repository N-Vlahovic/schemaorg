# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.600594
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .category_code import CategoryCode
from .medical_intangible import MedicalIntangible
from .text import Text


@dataclass
class MedicalCode(CategoryCode, MedicalIntangible):
    codeValue: Text | None
    codingSystem: Text | None
