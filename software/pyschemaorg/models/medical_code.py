# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584954
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.category_code import CategoryCode
from models.medical_intangible import MedicalIntangible
from models.text import Text


@dataclass
class MedicalCode(CategoryCode, MedicalIntangible):
    codeValue: Text | None
    codingSystem: Text | None
