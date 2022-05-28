# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.598109
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .media_manipulation_rating_enumeration import MediaManipulationRatingEnumeration
from .media_object import MediaObject
from .review import Review
from .text import Text
from .url import URL
from .web_page import WebPage


@dataclass
class MediaReview(Review):
    mediaAuthenticityCategory: MediaManipulationRatingEnumeration | None
    originalMediaContextDescription: Text | None
    originalMediaLink: MediaObject | URL | WebPage | None
