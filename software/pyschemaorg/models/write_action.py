# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.628387
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .create_action import CreateAction
from .language import Language
from .text import Text


@dataclass
class WriteAction(CreateAction):
    inLanguage: Language | Text | None
    language: Language | None
