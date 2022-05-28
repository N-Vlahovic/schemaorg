# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584918
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.category_code_set import CategoryCodeSet
from models.defined_term import DefinedTerm
from models.text import Text
from models.url import URL


@dataclass
class CategoryCode(DefinedTerm):
    codeValue: Text | None
    inCodeSet: CategoryCodeSet | URL | None
