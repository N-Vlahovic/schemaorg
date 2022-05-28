# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.581675
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .breadcrumb_list import BreadcrumbList
from .creative_work import CreativeWork
from .date import Date
from .image_object import ImageObject
from .organization import Organization
from .person import Person
from .speakable_specification import SpeakableSpecification
from .specialty import Specialty
from .text import Text
from .url import URL
from .web_page_element import WebPageElement


@dataclass
class WebPage(CreativeWork):
    breadcrumb: BreadcrumbList | Text | None
    lastReviewed: Date | None
    mainContentOfPage: WebPageElement | None
    primaryImageOfPage: ImageObject | None
    relatedLink: URL | None
    reviewedBy: Organization | Person | None
    significantLink: URL | None
    significantLinks: URL | None
    speakable: SpeakableSpecification | URL | None
    specialty: Specialty | None
