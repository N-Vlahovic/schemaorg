# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579036
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.article import Article
from models.text import Text


@dataclass
class NewsArticle(Article):
    dateline: Text | None
    printColumn: Text | None
    printEdition: Text | None
    printPage: Text | None
    printSection: Text | None
