# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584743
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.category_code import CategoryCode
from models.civic_structure import CivicStructure
from models.creative_work import CreativeWork
from models.data_feed import DataFeed
from models.dataset import Dataset
from models.date import Date
from models.date_time import DateTime
from models.government_service import GovernmentService
from models.local_business import LocalBusiness
from models.observation import Observation
from models.physical_activity_category import PhysicalActivityCategory
from models.text import Text
from models.thing import Thing
from models.url import URL
from models.web_content import WebContent


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
