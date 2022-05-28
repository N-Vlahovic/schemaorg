# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.580165
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .claim import Claim
from .creative_work import CreativeWork
from .date import Date
from .date_time import DateTime
from .distance import Distance
from .duration import Duration
from .geo_shape import GeoShape
from .media_subscription import MediaSubscription
from .news_article import NewsArticle
from .organization import Organization
from .place import Place
from .quantitative_value import QuantitativeValue
from .text import Text
from .time import Time
from .url import URL


@dataclass
class MediaObject(CreativeWork):
    associatedArticle: NewsArticle | None
    bitrate: Text | None
    contentSize: Text | None
    contentUrl: URL | None
    duration: Duration | None
    embedUrl: URL | None
    encodesCreativeWork: CreativeWork | None
    encodingFormat: Text | URL | None
    endTime: DateTime | Time | None
    height: Distance | QuantitativeValue | None
    ineligibleRegion: GeoShape | Place | Text | None
    interpretedAsClaim: Claim | None
    playerType: Text | None
    productionCompany: Organization | None
    regionsAllowed: Place | None
    requiresSubscription: Boolean | MediaSubscription | None
    sha256: Text | None
    startTime: DateTime | Time | None
    uploadDate: Date | None
    width: Distance | QuantitativeValue | None
