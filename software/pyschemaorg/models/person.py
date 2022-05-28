# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573118
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.brand import Brand
from models.contact_point import ContactPoint
from models.country import Country
from models.creative_work import CreativeWork
from models.date import Date
from models.defined_term import DefinedTerm
from models.demand import Demand
from models.distance import Distance
from models.educational_occupational_credential import EducationalOccupationalCredential
from models.educational_organization import EducationalOrganization
from models.event import Event
from models.gender_type import GenderType
from models.grant import Grant
from models.interaction_counter import InteractionCounter
from models.language import Language
from models.monetary_amount import MonetaryAmount
from models.occupation import Occupation
from models.offer import Offer
from models.offer_catalog import OfferCatalog
from models.organization import Organization
from models.ownership_info import OwnershipInfo
from models.place import Place
from models.postal_address import PostalAddress
from models.price_specification import PriceSpecification
from models.product import Product
from models.program_membership import ProgramMembership
from models.quantitative_value import QuantitativeValue
from models.text import Text
from models.thing import Thing
from models.url import URL


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
