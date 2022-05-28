# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576132
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.blog_posting import BlogPosting
from models.date_time import DateTime


@dataclass
class LiveBlogPosting(BlogPosting):
    coverageEndTime: DateTime | None
    coverageStartTime: DateTime | None
    liveBlogUpdate: BlogPosting | None
