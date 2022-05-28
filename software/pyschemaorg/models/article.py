# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.610130
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .integer import Integer
from .speakable_specification import SpeakableSpecification
from .text import Text
from .url import URL


@dataclass
class Article(CreativeWork):
    articleBody: Text | None
    articleSection: Text | None
    backstory: CreativeWork | Text | None
    pageEnd: Integer | Text | None
    pageStart: Integer | Text | None
    pagination: Text | None
    speakable: SpeakableSpecification | URL | None
    wordCount: Integer | None
