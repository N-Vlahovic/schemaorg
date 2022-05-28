# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582169
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.aggregate_rating import AggregateRating
from models.audience import Audience
from models.brand import Brand
from models.category_code import CategoryCode
from models.demand import Demand
from models.geo_shape import GeoShape
from models.government_benefits_type import GovernmentBenefitsType
from models.image_object import ImageObject
from models.intangible import Intangible
from models.offer import Offer
from models.offer_catalog import OfferCatalog
from models.opening_hours_specification import OpeningHoursSpecification
from models.organization import Organization
from models.person import Person
from models.physical_activity_category import PhysicalActivityCategory
from models.place import Place
from models.product import Product
from models.review import Review
from models.service_channel import ServiceChannel
from models.text import Text
from models.thing import Thing
from models.url import URL


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
