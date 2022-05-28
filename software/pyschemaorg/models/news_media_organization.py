# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577676
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.about_page import AboutPage
from models.article import Article
from models.creative_work import CreativeWork
from models.organization import Organization
from models.text import Text
from models.url import URL


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
