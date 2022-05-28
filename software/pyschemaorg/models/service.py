# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.595917
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .aggregate_rating import AggregateRating
from .audience import Audience
from .brand import Brand
from .category_code import CategoryCode
from .demand import Demand
from .geo_shape import GeoShape
from .government_benefits_type import GovernmentBenefitsType
from .image_object import ImageObject
from .intangible import Intangible
from .offer import Offer
from .offer_catalog import OfferCatalog
from .opening_hours_specification import OpeningHoursSpecification
from .organization import Organization
from .person import Person
from .physical_activity_category import PhysicalActivityCategory
from .place import Place
from .product import Product
from .review import Review
from .service_channel import ServiceChannel
from .text import Text
from .thing import Thing
from .url import URL


@dataclass
class Service(Intangible):
    aggregateRating: AggregateRating | None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None
    audience: Audience | None
    availableChannel: ServiceChannel | None
    award: Text | None
    brand: Brand | Organization | None
    broker: Organization | Person | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    hasOfferCatalog: OfferCatalog | None
    hoursAvailable: OpeningHoursSpecification | None
    isRelatedTo: Product | Service | None
    isSimilarTo: Product | Service | None
    logo: ImageObject | URL | None
    offers: Demand | Offer | None
    produces: Thing | None
    provider: Organization | Person | None
    providerMobility: Text | None
    review: Review | None
    serviceArea: AdministrativeArea | GeoShape | Place | None
    serviceAudience: Audience | None
    serviceOutput: Thing | None
    serviceType: GovernmentBenefitsType | Text | None
    slogan: Text | None
    termsOfService: Text | URL | None
