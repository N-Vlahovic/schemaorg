# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577835
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.about_page import AboutPage
from models.administrative_area import AdministrativeArea
from models.aggregate_rating import AggregateRating
from models.article import Article
from models.brand import Brand
from models.contact_point import ContactPoint
from models.creative_work import CreativeWork
from models.date import Date
from models.defined_term import DefinedTerm
from models.demand import Demand
from models.educational_occupational_credential import EducationalOccupationalCredential
from models.event import Event
from models.geo_shape import GeoShape
from models.grant import Grant
from models.image_object import ImageObject
from models.interaction_counter import InteractionCounter
from models.language import Language
from models.merchant_return_policy import MerchantReturnPolicy
from models.nonprofit_type import NonprofitType
from models.offer import Offer
from models.offer_catalog import OfferCatalog
from models.ownership_info import OwnershipInfo
from models.person import Person
from models.place import Place
from models.postal_address import PostalAddress
from models.product import Product
from models.product_return_policy import ProductReturnPolicy
from models.program_membership import ProgramMembership
from models.quantitative_value import QuantitativeValue
from models.review import Review
from models.text import Text
from models.thing import Thing
from models.url import URL
from models.virtual_location import VirtualLocation


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
