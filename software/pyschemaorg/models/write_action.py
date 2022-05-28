# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.601100
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.create_action import CreateAction
from models.language import Language
from models.text import Text


@dataclass
class WriteAction(CreateAction):
    inLanguage: Language | Text | None
    language: Language | None
