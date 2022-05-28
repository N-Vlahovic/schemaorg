# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.593954
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .critic_review import CriticReview
from .news_article import NewsArticle


@dataclass
class ReviewNewsArticle(CriticReview, NewsArticle):
    pass
