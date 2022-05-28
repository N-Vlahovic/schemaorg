# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.606964
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .language import Language
from .text import Text


@dataclass
class PronounceableText(Text):
    inLanguage: Language | Text | None
    phoneticText: Text | None
    speechToTextMarkup: Text | None
    textValue: Text | None
