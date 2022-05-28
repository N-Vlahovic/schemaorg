# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.600230
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .category_code import CategoryCode
from .civic_structure import CivicStructure
from .creative_work import CreativeWork
from .data_feed import DataFeed
from .dataset import Dataset
from .date import Date
from .date_time import DateTime
from .government_service import GovernmentService
from .local_business import LocalBusiness
from .observation import Observation
from .physical_activity_category import PhysicalActivityCategory
from .text import Text
from .thing import Thing
from .url import URL
from .web_content import WebContent


@dataclass
class SpecialAnnouncement(CreativeWork):
    announcementLocation: CivicStructure | LocalBusiness | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    datePosted: Date | DateTime | None
    diseasePreventionInfo: URL | WebContent | None
    diseaseSpreadStatistics: Dataset | Observation | URL | WebContent | None
    gettingTestedInfo: URL | WebContent | None
    governmentBenefitsInfo: GovernmentService | None
    newsUpdatesAndGuidelines: URL | WebContent | None
    publicTransportClosuresInfo: URL | WebContent | None
    quarantineGuidelines: URL | WebContent | None
    schoolClosuresInfo: URL | WebContent | None
    travelBans: URL | WebContent | None
    webFeed: DataFeed | URL | None
