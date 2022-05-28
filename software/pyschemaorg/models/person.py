# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.579225
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .brand import Brand
from .contact_point import ContactPoint
from .country import Country
from .creative_work import CreativeWork
from .date import Date
from .defined_term import DefinedTerm
from .demand import Demand
from .distance import Distance
from .educational_occupational_credential import EducationalOccupationalCredential
from .educational_organization import EducationalOrganization
from .event import Event
from .gender_type import GenderType
from .grant import Grant
from .interaction_counter import InteractionCounter
from .language import Language
from .monetary_amount import MonetaryAmount
from .occupation import Occupation
from .offer import Offer
from .offer_catalog import OfferCatalog
from .organization import Organization
from .ownership_info import OwnershipInfo
from .place import Place
from .postal_address import PostalAddress
from .price_specification import PriceSpecification
from .product import Product
from .program_membership import ProgramMembership
from .quantitative_value import QuantitativeValue
from .text import Text
from .thing import Thing
from .url import URL


@dataclass
class Person(Thing):
    additionalName: Text | None
    address: PostalAddress | Text | None
    affiliation: Organization | None
    alumniOf: EducationalOrganization | Organization | None
    award: Text | None
    awards: Text | None
    birthDate: Date | None
    birthPlace: Place | None
    brand: Brand | Organization | None
    callSign: Text | None
    children: Person | None
    colleague: Person | URL | None
    colleagues: Person | None
    contactPoint: ContactPoint | None
    contactPoints: ContactPoint | None
    deathDate: Date | None
    deathPlace: Place | None
    duns: Text | None
    email: Text | None
    familyName: Text | None
    faxNumber: Text | None
    follows: Person | None
    funder: Organization | Person | None
    funding: Grant | None
    gender: GenderType | Text | None
    givenName: Text | None
    globalLocationNumber: Text | None
    hasCredential: EducationalOccupationalCredential | None
    hasOccupation: Occupation | None
    hasOfferCatalog: OfferCatalog | None
    hasPOS: Place | None
    height: Distance | QuantitativeValue | None
    homeLocation: ContactPoint | Place | None
    honorificPrefix: Text | None
    honorificSuffix: Text | None
    interactionStatistic: InteractionCounter | None
    isicV4: Text | None
    jobTitle: DefinedTerm | Text | None
    knows: Person | None
    knowsAbout: Text | Thing | URL | None
    knowsLanguage: Language | Text | None
    makesOffer: Offer | None
    memberOf: Organization | ProgramMembership | None
    naics: Text | None
    nationality: Country | None
    netWorth: MonetaryAmount | PriceSpecification | None
    owns: OwnershipInfo | Product | None
    parent: Person | None
    parents: Person | None
    performerIn: Event | None
    publishingPrinciples: CreativeWork | URL | None
    relatedTo: Person | None
    seeks: Demand | None
    sibling: Person | None
    siblings: Person | None
    sponsor: Organization | Person | None
    spouse: Person | None
    taxID: Text | None
    telephone: Text | None
    vatID: Text | None
    weight: QuantitativeValue | None
    workLocation: ContactPoint | Place | None
    worksFor: Organization | None
