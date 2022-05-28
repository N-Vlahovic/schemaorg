# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.584765
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .blog_posting import BlogPosting
from .date_time import DateTime


@dataclass
class LiveBlogPosting(BlogPosting):
    coverageEndTime: DateTime | None
    coverageStartTime: DateTime | None
    liveBlogUpdate: BlogPosting | None
