# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575595
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.aggregate_rating import AggregateRating
from models.alignment_object import AlignmentObject
from models.audience import Audience
from models.audio_object import AudioObject
from models.boolean import Boolean
from models.claim import Claim
from models.clip import Clip
from models.comment import Comment
from models.correction_comment import CorrectionComment
from models.country import Country
from models.date import Date
from models.date_time import DateTime
from models.defined_term import DefinedTerm
from models.demand import Demand
from models.duration import Duration
from models.event import Event
from models.grant import Grant
from models.integer import Integer
from models.interaction_counter import InteractionCounter
from models.item_list import ItemList
from models.language import Language
from models.media_object import MediaObject
from models.music_recording import MusicRecording
from models.number import Number
from models.offer import Offer
from models.organization import Organization
from models.person import Person
from models.place import Place
from models.product import Product
from models.publication_event import PublicationEvent
from models.quantitative_value import QuantitativeValue
from models.rating import Rating
from models.review import Review
from models.size_specification import SizeSpecification
from models.text import Text
from models.thing import Thing
from models.url import URL
from models.video_object import VideoObject
from models.web_page import WebPage


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
