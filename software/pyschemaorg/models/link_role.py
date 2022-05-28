# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.592967
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.language import Language
from models.role import Role
from models.text import Text


@dataclass
class LinkRole(Role):
    inLanguage: Language | Text | None
    linkRelationship: Text | None
