# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.587962
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .about_page import AboutPage
from .article import Article
from .creative_work import CreativeWork
from .organization import Organization
from .text import Text
from .url import URL


@dataclass
class NewsMediaOrganization(Organization):
    actionableFeedbackPolicy: CreativeWork | URL | None
    correctionsPolicy: CreativeWork | URL | None
    diversityPolicy: CreativeWork | URL | None
    diversityStaffingReport: Article | URL | None
    ethicsPolicy: CreativeWork | URL | None
    masthead: CreativeWork | URL | None
    missionCoveragePrioritiesPolicy: CreativeWork | URL | None
    noBylinesPolicy: CreativeWork | URL | None
    ownershipFundingInfo: AboutPage | CreativeWork | Text | URL | None
    unnamedSourcesPolicy: CreativeWork | URL | None
    verificationFactCheckingPolicy: CreativeWork | URL | None
