# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.583769
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .aggregate_rating import AggregateRating
from .alignment_object import AlignmentObject
from .audience import Audience
from .audio_object import AudioObject
from .boolean import Boolean
from .claim import Claim
from .clip import Clip
from .comment import Comment
from .correction_comment import CorrectionComment
from .country import Country
from .date import Date
from .date_time import DateTime
from .defined_term import DefinedTerm
from .demand import Demand
from .duration import Duration
from .event import Event
from .grant import Grant
from .integer import Integer
from .interaction_counter import InteractionCounter
from .item_list import ItemList
from .language import Language
from .media_object import MediaObject
from .music_recording import MusicRecording
from .number import Number
from .offer import Offer
from .organization import Organization
from .person import Person
from .place import Place
from .product import Product
from .publication_event import PublicationEvent
from .quantitative_value import QuantitativeValue
from .rating import Rating
from .review import Review
from .size_specification import SizeSpecification
from .text import Text
from .thing import Thing
from .url import URL
from .video_object import VideoObject
from .web_page import WebPage


@dataclass
class CreativeWork(Thing):
    about: Thing | None
    abstract: Text | None
    accessMode: Text | None
    accessModeSufficient: ItemList | None
    accessibilityAPI: Text | None
    accessibilityControl: Text | None
    accessibilityFeature: Text | None
    accessibilityHazard: Text | None
    accessibilitySummary: Text | None
    accountablePerson: Person | None
    acquireLicensePage: CreativeWork | URL | None
    aggregateRating: AggregateRating | None
    alternativeHeadline: Text | None
    archivedAt: URL | WebPage | None
    assesses: DefinedTerm | Text | None
    associatedMedia: MediaObject | None
    audience: Audience | None
    audio: AudioObject | Clip | MusicRecording | None
    author: Organization | Person | None
    award: Text | None
    awards: Text | None
    character: Person | None
    citation: CreativeWork | Text | None
    comment: Comment | None
    commentCount: Integer | None
    conditionsOfAccess: Text | None
    contentLocation: Place | None
    contentRating: Rating | Text | None
    contentReferenceTime: DateTime | None
    contributor: Organization | Person | None
    copyrightHolder: Organization | Person | None
    copyrightNotice: Text | None
    copyrightYear: Number | None
    correction: CorrectionComment | Text | URL | None
    countryOfOrigin: Country | None
    creativeWorkStatus: DefinedTerm | Text | None
    creator: Organization | Person | None
    creditText: Text | None
    dateCreated: Date | DateTime | None
    dateModified: Date | DateTime | None
    datePublished: Date | DateTime | None
    discussionUrl: URL | None
    editEIDR: Text | URL | None
    editor: Person | None
    educationalAlignment: AlignmentObject | None
    educationalLevel: DefinedTerm | Text | URL | None
    educationalUse: DefinedTerm | Text | None
    encoding: MediaObject | None
    encodingFormat: Text | URL | None
    encodings: MediaObject | None
    exampleOfWork: CreativeWork | None
    expires: Date | None
    fileFormat: Text | URL | None
    funder: Organization | Person | None
    funding: Grant | None
    genre: Text | URL | None
    hasPart: CreativeWork | None
    headline: Text | None
    inLanguage: Language | Text | None
    interactionStatistic: InteractionCounter | None
    interactivityType: Text | None
    interpretedAsClaim: Claim | None
    isAccessibleForFree: Boolean | None
    isBasedOn: CreativeWork | Product | URL | None
    isBasedOnUrl: CreativeWork | Product | URL | None
    isFamilyFriendly: Boolean | None
    isPartOf: CreativeWork | URL | None
    keywords: DefinedTerm | Text | URL | None
    learningResourceType: DefinedTerm | Text | None
    license: CreativeWork | URL | None
    locationCreated: Place | None
    mainEntity: Thing | None
    maintainer: Organization | Person | None
    material: Product | Text | URL | None
    materialExtent: QuantitativeValue | Text | None
    mentions: Thing | None
    offers: Demand | Offer | None
    pattern: DefinedTerm | Text | None
    position: Integer | Text | None
    producer: Organization | Person | None
    provider: Organization | Person | None
    publication: PublicationEvent | None
    publisher: Organization | Person | None
    publisherImprint: Organization | None
    publishingPrinciples: CreativeWork | URL | None
    recordedAt: Event | None
    releasedEvent: PublicationEvent | None
    review: Review | None
    reviews: Review | None
    schemaVersion: Text | URL | None
    sdDatePublished: Date | None
    sdLicense: CreativeWork | URL | None
    sdPublisher: Organization | Person | None
    size: DefinedTerm | QuantitativeValue | SizeSpecification | Text | None
    sourceOrganization: Organization | None
    spatial: Place | None
    spatialCoverage: Place | None
    sponsor: Organization | Person | None
    teaches: DefinedTerm | Text | None
    temporal: DateTime | Text | None
    temporalCoverage: DateTime | Text | URL | None
    text: Text | None
    thumbnailUrl: URL | None
    timeRequired: Duration | None
    translationOfWork: CreativeWork | None
    translator: Organization | Person | None
    typicalAgeRange: Text | None
    usageInfo: CreativeWork | URL | None
    version: Number | Text | None
    video: Clip | VideoObject | None
    workExample: CreativeWork | None
    workTranslation: CreativeWork | None
