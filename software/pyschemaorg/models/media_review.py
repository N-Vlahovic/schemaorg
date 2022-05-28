# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.583543
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.media_manipulation_rating_enumeration import MediaManipulationRatingEnumeration
from models.media_object import MediaObject
from models.review import Review
from models.text import Text
from models.url import URL
from models.web_page import WebPage


@dataclass
class MediaReview(Review):
    mediaAuthenticityCategory: MediaManipulationRatingEnumeration | None
    originalMediaContextDescription: Text | None
    originalMediaLink: MediaObject | URL | WebPage | None
