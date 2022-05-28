# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574410
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.breadcrumb_list import BreadcrumbList
from models.creative_work import CreativeWork
from models.date import Date
from models.image_object import ImageObject
from models.organization import Organization
from models.person import Person
from models.speakable_specification import SpeakableSpecification
from models.specialty import Specialty
from models.text import Text
from models.url import URL
from models.web_page_element import WebPageElement


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
