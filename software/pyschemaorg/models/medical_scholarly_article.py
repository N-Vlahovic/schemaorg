# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582408
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .scholarly_article import ScholarlyArticle
from .text import Text


@dataclass
class MedicalScholarlyArticle(ScholarlyArticle):
    publicationType: Text | None
