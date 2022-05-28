# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.600532
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .category_code_set import CategoryCodeSet
from .defined_term import DefinedTerm
from .text import Text
from .url import URL


@dataclass
class CategoryCode(DefinedTerm):
    codeValue: Text | None
    inCodeSet: CategoryCodeSet | URL | None
