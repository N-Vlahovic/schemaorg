# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573613
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.claim import Claim
from models.creative_work import CreativeWork
from models.date import Date
from models.date_time import DateTime
from models.distance import Distance
from models.duration import Duration
from models.geo_shape import GeoShape
from models.media_subscription import MediaSubscription
from models.news_article import NewsArticle
from models.organization import Organization
from models.place import Place
from models.quantitative_value import QuantitativeValue
from models.text import Text
from models.time import Time
from models.url import URL


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
