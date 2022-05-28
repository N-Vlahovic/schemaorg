# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.588330
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .about_page import AboutPage
from .administrative_area import AdministrativeArea
from .aggregate_rating import AggregateRating
from .article import Article
from .brand import Brand
from .contact_point import ContactPoint
from .creative_work import CreativeWork
from .date import Date
from .defined_term import DefinedTerm
from .demand import Demand
from .educational_occupational_credential import EducationalOccupationalCredential
from .event import Event
from .geo_shape import GeoShape
from .grant import Grant
from .image_object import ImageObject
from .interaction_counter import InteractionCounter
from .language import Language
from .merchant_return_policy import MerchantReturnPolicy
from .nonprofit_type import NonprofitType
from .offer import Offer
from .offer_catalog import OfferCatalog
from .ownership_info import OwnershipInfo
from .person import Person
from .place import Place
from .postal_address import PostalAddress
from .product import Product
from .product_return_policy import ProductReturnPolicy
from .program_membership import ProgramMembership
from .quantitative_value import QuantitativeValue
from .review import Review
from .text import Text
from .thing import Thing
from .url import URL
from .virtual_location import VirtualLocation


@dataclass
class Organization(Thing):
    actionableFeedbackPolicy: CreativeWork | URL | None
    address: PostalAddress | Text | None
    aggregateRating: AggregateRating | None
    alumni: Person | None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None
    award: Text | None
    awards: Text | None
    brand: Brand | Organization | None
    contactPoint: ContactPoint | None
    contactPoints: ContactPoint | None
    correctionsPolicy: CreativeWork | URL | None
    department: Organization | None
    dissolutionDate: Date | None
    diversityPolicy: CreativeWork | URL | None
    diversityStaffingReport: Article | URL | None
    duns: Text | None
    email: Text | None
    employee: Person | None
    employees: Person | None
    ethicsPolicy: CreativeWork | URL | None
    event: Event | None
    events: Event | None
    faxNumber: Text | None
    founder: Person | None
    founders: Person | None
    foundingDate: Date | None
    foundingLocation: Place | None
    funder: Organization | Person | None
    funding: Grant | None
    globalLocationNumber: Text | None
    hasCredential: EducationalOccupationalCredential | None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None
    hasOfferCatalog: OfferCatalog | None
    hasPOS: Place | None
    hasProductReturnPolicy: ProductReturnPolicy | None
    interactionStatistic: InteractionCounter | None
    isicV4: Text | None
    iso6523Code: Text | None
    keywords: DefinedTerm | Text | URL | None
    knowsAbout: Text | Thing | URL | None
    knowsLanguage: Language | Text | None
    legalName: Text | None
    leiCode: Text | None
    location: Place | PostalAddress | Text | VirtualLocation | None
    logo: ImageObject | URL | None
    makesOffer: Offer | None
    member: Organization | Person | None
    memberOf: Organization | ProgramMembership | None
    members: Organization | Person | None
    naics: Text | None
    nonprofitStatus: NonprofitType | None
    numberOfEmployees: QuantitativeValue | None
    ownershipFundingInfo: AboutPage | CreativeWork | Text | URL | None
    owns: OwnershipInfo | Product | None
    parentOrganization: Organization | None
    publishingPrinciples: CreativeWork | URL | None
    review: Review | None
    reviews: Review | None
    seeks: Demand | None
    serviceArea: AdministrativeArea | GeoShape | Place | None
    slogan: Text | None
    sponsor: Organization | Person | None
    subOrganization: Organization | None
    taxID: Text | None
    telephone: Text | None
    unnamedSourcesPolicy: CreativeWork | URL | None
    vatID: Text | None
