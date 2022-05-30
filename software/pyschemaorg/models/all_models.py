# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-30T19:30:11.009357
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. https://github.com/n-vlahovic

from __future__ import annotations
import datetime
from dataclasses import dataclass

from models.abstract_base import AbstractBase


@dataclass
class Thing(AbstractBase):
    additionalType: URL | None = None
    alternateName: str | None = None
    description: str | None = None
    disambiguatingDescription: str | None = None
    identifier: PropertyValue | URL | str | None = None
    image: ImageObject | URL | None = None
    mainEntityOfPage: CreativeWork | URL | None = None
    name: str | None = None
    potentialAction: Action | None = None
    sameAs: URL | None = None
    subjectOf: CreativeWork | Event | None = None
    url: URL | None = None


@dataclass
class Person(Thing):
    additionalName: str | None = None
    address: PostalAddress | str | None = None
    affiliation: Organization | None = None
    alumniOf: EducationalOrganization | Organization | None = None
    award: str | None = None
    awards: str | None = None
    birthDate: datetime.date | None = None
    birthPlace: Place | None = None
    brand: Brand | Organization | None = None
    callSign: str | None = None
    children: Person | None = None
    colleague: Person | URL | None = None
    colleagues: Person | None = None
    contactPoint: ContactPoint | None = None
    contactPoints: ContactPoint | None = None
    deathDate: datetime.date | None = None
    deathPlace: Place | None = None
    duns: str | None = None
    email: str | None = None
    familyName: str | None = None
    faxNumber: str | None = None
    follows: Person | None = None
    funder: Organization | Person | None = None
    funding: Grant | None = None
    gender: GenderType | str | None = None
    givenName: str | None = None
    globalLocationNumber: str | None = None
    hasCredential: EducationalOccupationalCredential | None = None
    hasOccupation: Occupation | None = None
    hasOfferCatalog: OfferCatalog | None = None
    hasPOS: Place | None = None
    height: Distance | QuantitativeValue | None = None
    homeLocation: ContactPoint | Place | None = None
    honorificPrefix: str | None = None
    honorificSuffix: str | None = None
    interactionStatistic: InteractionCounter | None = None
    isicV4: str | None = None
    jobTitle: DefinedTerm | str | None = None
    knows: Person | None = None
    knowsAbout: Thing | URL | str | None = None
    knowsLanguage: Language | str | None = None
    makesOffer: Offer | None = None
    memberOf: Organization | ProgramMembership | None = None
    naics: str | None = None
    nationality: Country | None = None
    netWorth: MonetaryAmount | PriceSpecification | None = None
    owns: OwnershipInfo | Product | None = None
    parent: Person | None = None
    parents: Person | None = None
    performerIn: Event | None = None
    publishingPrinciples: CreativeWork | URL | None = None
    relatedTo: Person | None = None
    seeks: Demand | None = None
    sibling: Person | None = None
    siblings: Person | None = None
    sponsor: Organization | Person | None = None
    spouse: Person | None = None
    taxID: str | None = None
    telephone: str | None = None
    vatID: str | None = None
    weight: QuantitativeValue | None = None
    workLocation: ContactPoint | Place | None = None
    worksFor: Organization | None = None


@dataclass
class Taxon(Thing):
    childTaxon: Taxon | URL | str | None = None
    hasDefinedTerm: DefinedTerm | None = None
    parentTaxon: Taxon | URL | str | None = None
    taxonRank: PropertyValue | URL | str | None = None


@dataclass
class CreativeWork(Thing):
    about: Thing | None = None
    abstract: str | None = None
    accessMode: str | None = None
    accessModeSufficient: ItemList | None = None
    accessibilityAPI: str | None = None
    accessibilityControl: str | None = None
    accessibilityFeature: str | None = None
    accessibilityHazard: str | None = None
    accessibilitySummary: str | None = None
    accountablePerson: Person | None = None
    acquireLicensePage: CreativeWork | URL | None = None
    aggregateRating: AggregateRating | None = None
    alternativeHeadline: str | None = None
    archivedAt: URL | WebPage | None = None
    assesses: DefinedTerm | str | None = None
    associatedMedia: MediaObject | None = None
    audience: Audience | None = None
    audio: AudioObject | Clip | MusicRecording | None = None
    author: Organization | Person | None = None
    award: str | None = None
    awards: str | None = None
    character: Person | None = None
    citation: CreativeWork | str | None = None
    comment: Comment | None = None
    commentCount: Integer | None = None
    conditionsOfAccess: str | None = None
    contentLocation: Place | None = None
    contentRating: Rating | str | None = None
    contentReferenceTime: datetime.datetime | None = None
    contributor: Organization | Person | None = None
    copyrightHolder: Organization | Person | None = None
    copyrightNotice: str | None = None
    copyrightYear: float | None = None
    correction: CorrectionComment | URL | str | None = None
    countryOfOrigin: Country | None = None
    creativeWorkStatus: DefinedTerm | str | None = None
    creator: Organization | Person | None = None
    creditText: str | None = None
    dateCreated: datetime.date | datetime.datetime | None = None
    dateModified: datetime.date | datetime.datetime | None = None
    datePublished: datetime.date | datetime.datetime | None = None
    discussionUrl: URL | None = None
    editEIDR: URL | str | None = None
    editor: Person | None = None
    educationalAlignment: AlignmentObject | None = None
    educationalLevel: DefinedTerm | URL | str | None = None
    educationalUse: DefinedTerm | str | None = None
    encoding: MediaObject | None = None
    encodingFormat: URL | str | None = None
    encodings: MediaObject | None = None
    exampleOfWork: CreativeWork | None = None
    expires: datetime.date | None = None
    fileFormat: URL | str | None = None
    funder: Organization | Person | None = None
    funding: Grant | None = None
    genre: URL | str | None = None
    hasPart: CreativeWork | None = None
    headline: str | None = None
    inLanguage: Language | str | None = None
    interactionStatistic: InteractionCounter | None = None
    interactivityType: str | None = None
    interpretedAsClaim: Claim | None = None
    isAccessibleForFree: bool | None = None
    isBasedOn: CreativeWork | Product | URL | None = None
    isBasedOnUrl: CreativeWork | Product | URL | None = None
    isFamilyFriendly: bool | None = None
    isPartOf: CreativeWork | URL | None = None
    keywords: DefinedTerm | URL | str | None = None
    learningResourceType: DefinedTerm | str | None = None
    license: CreativeWork | URL | None = None
    locationCreated: Place | None = None
    mainEntity: Thing | None = None
    maintainer: Organization | Person | None = None
    material: Product | URL | str | None = None
    materialExtent: QuantitativeValue | str | None = None
    mentions: Thing | None = None
    offers: Demand | Offer | None = None
    pattern: DefinedTerm | str | None = None
    position: Integer | str | None = None
    producer: Organization | Person | None = None
    provider: Organization | Person | None = None
    publication: PublicationEvent | None = None
    publisher: Organization | Person | None = None
    publisherImprint: Organization | None = None
    publishingPrinciples: CreativeWork | URL | None = None
    recordedAt: Event | None = None
    releasedEvent: PublicationEvent | None = None
    review: Review | None = None
    reviews: Review | None = None
    schemaVersion: URL | str | None = None
    sdDatePublished: datetime.date | None = None
    sdLicense: CreativeWork | URL | None = None
    sdPublisher: Organization | Person | None = None
    size: DefinedTerm | QuantitativeValue | SizeSpecification | str | None = None
    sourceOrganization: Organization | None = None
    spatial: Place | None = None
    spatialCoverage: Place | None = None
    sponsor: Organization | Person | None = None
    teaches: DefinedTerm | str | None = None
    temporal: datetime.datetime | str | None = None
    temporalCoverage: URL | datetime.datetime | str | None = None
    text: str | None = None
    thumbnailUrl: URL | None = None
    timeRequired: Duration | None = None
    translationOfWork: CreativeWork | None = None
    translator: Organization | Person | None = None
    typicalAgeRange: str | None = None
    usageInfo: CreativeWork | URL | None = None
    version: float | str | None = None
    video: Clip | VideoObject | None = None
    workExample: CreativeWork | None = None
    workTranslation: CreativeWork | None = None


@dataclass
class Product(Thing):
    additionalProperty: PropertyValue | None = None
    aggregateRating: AggregateRating | None = None
    audience: Audience | None = None
    award: str | None = None
    awards: str | None = None
    brand: Brand | Organization | None = None
    category: CategoryCode | PhysicalActivityCategory | Thing | URL | str | None = None
    color: str | None = None
    countryOfAssembly: str | None = None
    countryOfLastProcessing: str | None = None
    countryOfOrigin: Country | None = None
    depth: Distance | QuantitativeValue | None = None
    funding: Grant | None = None
    gtin: str | None = None
    gtin12: str | None = None
    gtin13: str | None = None
    gtin14: str | None = None
    gtin8: str | None = None
    hasAdultConsideration: AdultOrientedEnumeration | None = None
    hasEnergyConsumptionDetails: EnergyConsumptionDetails | None = None
    hasMeasurement: QuantitativeValue | None = None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None = None
    hasProductReturnPolicy: ProductReturnPolicy | None = None
    height: Distance | QuantitativeValue | None = None
    inProductGroupWithID: str | None = None
    isAccessoryOrSparePartFor: Product | None = None
    isConsumableFor: Product | None = None
    isFamilyFriendly: bool | None = None
    isRelatedTo: Product | Service | None = None
    isSimilarTo: Product | Service | None = None
    isVariantOf: ProductGroup | ProductModel | None = None
    itemCondition: OfferItemCondition | None = None
    keywords: DefinedTerm | URL | str | None = None
    logo: ImageObject | URL | None = None
    manufacturer: Organization | None = None
    material: Product | URL | str | None = None
    model: ProductModel | str | None = None
    mpn: str | None = None
    nsn: str | None = None
    offers: Demand | Offer | None = None
    pattern: DefinedTerm | str | None = None
    productID: str | None = None
    productionDate: datetime.date | None = None
    purchaseDate: datetime.date | None = None
    releaseDate: datetime.date | None = None
    review: Review | None = None
    reviews: Review | None = None
    size: DefinedTerm | QuantitativeValue | SizeSpecification | str | None = None
    sku: str | None = None
    slogan: str | None = None
    weight: QuantitativeValue | None = None
    width: Distance | QuantitativeValue | None = None


@dataclass
class Organization(Thing):
    actionableFeedbackPolicy: CreativeWork | URL | None = None
    address: PostalAddress | str | None = None
    aggregateRating: AggregateRating | None = None
    alumni: Person | None = None
    areaServed: AdministrativeArea | GeoShape | Place | str | None = None
    award: str | None = None
    awards: str | None = None
    brand: Brand | Organization | None = None
    contactPoint: ContactPoint | None = None
    contactPoints: ContactPoint | None = None
    correctionsPolicy: CreativeWork | URL | None = None
    department: Organization | None = None
    dissolutionDate: datetime.date | None = None
    diversityPolicy: CreativeWork | URL | None = None
    diversityStaffingReport: Article | URL | None = None
    duns: str | None = None
    email: str | None = None
    employee: Person | None = None
    employees: Person | None = None
    ethicsPolicy: CreativeWork | URL | None = None
    event: Event | None = None
    events: Event | None = None
    faxNumber: str | None = None
    founder: Person | None = None
    founders: Person | None = None
    foundingDate: datetime.date | None = None
    foundingLocation: Place | None = None
    funder: Organization | Person | None = None
    funding: Grant | None = None
    globalLocationNumber: str | None = None
    hasCredential: EducationalOccupationalCredential | None = None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None = None
    hasOfferCatalog: OfferCatalog | None = None
    hasPOS: Place | None = None
    hasProductReturnPolicy: ProductReturnPolicy | None = None
    interactionStatistic: InteractionCounter | None = None
    isicV4: str | None = None
    iso6523Code: str | None = None
    keywords: DefinedTerm | URL | str | None = None
    knowsAbout: Thing | URL | str | None = None
    knowsLanguage: Language | str | None = None
    legalName: str | None = None
    leiCode: str | None = None
    location: Place | PostalAddress | VirtualLocation | str | None = None
    logo: ImageObject | URL | None = None
    makesOffer: Offer | None = None
    member: Organization | Person | None = None
    memberOf: Organization | ProgramMembership | None = None
    members: Organization | Person | None = None
    naics: str | None = None
    nonprofitStatus: NonprofitType | None = None
    numberOfEmployees: QuantitativeValue | None = None
    ownershipFundingInfo: AboutPage | CreativeWork | URL | str | None = None
    owns: OwnershipInfo | Product | None = None
    parentOrganization: Organization | None = None
    publishingPrinciples: CreativeWork | URL | None = None
    review: Review | None = None
    reviews: Review | None = None
    seeks: Demand | None = None
    serviceArea: AdministrativeArea | GeoShape | Place | None = None
    slogan: str | None = None
    sponsor: Organization | Person | None = None
    subOrganization: Organization | None = None
    taxID: str | None = None
    telephone: str | None = None
    unnamedSourcesPolicy: CreativeWork | URL | None = None
    vatID: str | None = None


@dataclass
class Event(Thing):
    about: Thing | None = None
    actor: Person | None = None
    aggregateRating: AggregateRating | None = None
    attendee: Organization | Person | None = None
    attendees: Organization | Person | None = None
    audience: Audience | None = None
    composer: Organization | Person | None = None
    contributor: Organization | Person | None = None
    director: Person | None = None
    doorTime: datetime.datetime | datetime.time | None = None
    duration: Duration | None = None
    endDate: datetime.date | datetime.datetime | None = None
    eventAttendanceMode: EventAttendanceModeEnumeration | None = None
    eventSchedule: Schedule | None = None
    eventStatus: EventStatusType | None = None
    funder: Organization | Person | None = None
    funding: Grant | None = None
    inLanguage: Language | str | None = None
    isAccessibleForFree: bool | None = None
    keywords: DefinedTerm | URL | str | None = None
    location: Place | PostalAddress | VirtualLocation | str | None = None
    maximumAttendeeCapacity: Integer | None = None
    maximumPhysicalAttendeeCapacity: Integer | None = None
    maximumVirtualAttendeeCapacity: Integer | None = None
    offers: Demand | Offer | None = None
    organizer: Organization | Person | None = None
    performer: Organization | Person | None = None
    performers: Organization | Person | None = None
    previousStartDate: datetime.date | None = None
    recordedIn: CreativeWork | None = None
    remainingAttendeeCapacity: Integer | None = None
    review: Review | None = None
    sponsor: Organization | Person | None = None
    startDate: datetime.date | datetime.datetime | None = None
    subEvent: Event | None = None
    subEvents: Event | None = None
    superEvent: Event | None = None
    translator: Organization | Person | None = None
    typicalAgeRange: str | None = None
    workFeatured: CreativeWork | None = None
    workPerformed: CreativeWork | None = None


@dataclass
class MedicalEntity(Thing):
    code: MedicalCode | None = None
    funding: Grant | None = None
    guideline: MedicalGuideline | None = None
    legalStatus: DrugLegalStatus | MedicalEnumeration | str | None = None
    medicineSystem: MedicineSystem | None = None
    recognizingAuthority: Organization | None = None
    relevantSpecialty: MedicalSpecialty | None = None
    study: MedicalStudy | None = None


@dataclass
class Place(Thing):
    additionalProperty: PropertyValue | None = None
    address: PostalAddress | str | None = None
    aggregateRating: AggregateRating | None = None
    amenityFeature: LocationFeatureSpecification | None = None
    branchCode: str | None = None
    containedIn: Place | None = None
    containedInPlace: Place | None = None
    containsPlace: Place | None = None
    event: Event | None = None
    events: Event | None = None
    faxNumber: str | None = None
    geo: GeoCoordinates | GeoShape | None = None
    geoContains: GeospatialGeometry | Place | None = None
    geoCoveredBy: GeospatialGeometry | Place | None = None
    geoCovers: GeospatialGeometry | Place | None = None
    geoCrosses: GeospatialGeometry | Place | None = None
    geoDisjoint: GeospatialGeometry | Place | None = None
    geoEquals: GeospatialGeometry | Place | None = None
    geoIntersects: GeospatialGeometry | Place | None = None
    geoOverlaps: GeospatialGeometry | Place | None = None
    geoTouches: GeospatialGeometry | Place | None = None
    geoWithin: GeospatialGeometry | Place | None = None
    globalLocationNumber: str | None = None
    hasDriveThroughService: bool | None = None
    hasMap: Map | URL | None = None
    isAccessibleForFree: bool | None = None
    isicV4: str | None = None
    keywords: DefinedTerm | URL | str | None = None
    latitude: float | str | None = None
    logo: ImageObject | URL | None = None
    longitude: float | str | None = None
    map: URL | None = None
    maps: URL | None = None
    maximumAttendeeCapacity: Integer | None = None
    openingHoursSpecification: OpeningHoursSpecification | None = None
    photo: ImageObject | Photograph | None = None
    photos: ImageObject | Photograph | None = None
    publicAccess: bool | None = None
    review: Review | None = None
    reviews: Review | None = None
    slogan: str | None = None
    smokingAllowed: bool | None = None
    specialOpeningHoursSpecification: OpeningHoursSpecification | None = None
    telephone: str | None = None
    tourBookingPage: URL | None = None


@dataclass
class Action(Thing):
    actionStatus: ActionStatusType | None = None
    agent: Organization | Person | None = None
    endTime: datetime.datetime | datetime.time | None = None
    error: Thing | None = None
    instrument: Thing | None = None
    location: Place | PostalAddress | VirtualLocation | str | None = None
    object: Thing | None = None
    participant: Organization | Person | None = None
    provider: Organization | Person | None = None
    result: Thing | None = None
    startTime: datetime.datetime | datetime.time | None = None
    target: EntryPoint | None = None


@dataclass
class BioChemEntity(Thing):
    associatedDisease: MedicalCondition | PropertyValue | URL | None = None
    bioChemInteraction: BioChemEntity | None = None
    bioChemSimilarity: BioChemEntity | None = None
    biologicalRole: DefinedTerm | None = None
    funding: Grant | None = None
    hasBioChemEntityPart: BioChemEntity | None = None
    hasMolecularFunction: DefinedTerm | PropertyValue | URL | None = None
    hasRepresentation: PropertyValue | URL | str | None = None
    isEncodedByBioChemEntity: Gene | None = None
    isInvolvedInBiologicalProcess: DefinedTerm | PropertyValue | URL | None = None
    isLocatedInSubcellularLocation: DefinedTerm | PropertyValue | URL | None = None
    isPartOfBioChemEntity: BioChemEntity | None = None
    taxonomicRange: DefinedTerm | Taxon | URL | str | None = None


@dataclass
class Intangible(Thing):
    pass


@dataclass
class StupidType(Thing):
    stupidProperty: QuantitativeValue | None = None


@dataclass
class DataType(AbstractBase):
    pass


@dataclass
class Integer(float):
    pass


@dataclass
class Float(float):
    pass


@dataclass
class URL(str):
    pass


@dataclass
class PronounceableText(str):
    inLanguage: Language | str | None = None
    phoneticText: str | None = None
    speechToTextMarkup: str | None = None
    textValue: str | None = None


@dataclass
class CssSelectorType(str):
    pass


@dataclass
class XPathType(str):
    pass


@dataclass
class Accommodation(Place):
    accommodationCategory: str | None = None
    accommodationFloorPlan: FloorPlan | None = None
    amenityFeature: LocationFeatureSpecification | None = None
    floorLevel: str | None = None
    floorSize: QuantitativeValue | None = None
    leaseLength: Duration | QuantitativeValue | None = None
    numberOfBathroomsTotal: Integer | None = None
    numberOfBedrooms: QuantitativeValue | float | None = None
    numberOfFullBathrooms: float | None = None
    numberOfPartialBathrooms: float | None = None
    numberOfRooms: QuantitativeValue | float | None = None
    permittedUsage: str | None = None
    petsAllowed: bool | str | None = None
    tourBookingPage: URL | None = None
    yearBuilt: float | None = None


@dataclass
class Apartment(Accommodation):
    numberOfRooms: QuantitativeValue | float | None = None
    occupancy: QuantitativeValue | None = None


@dataclass
class House(Accommodation):
    numberOfRooms: QuantitativeValue | float | None = None


@dataclass
class Suite(Accommodation):
    bed: BedDetails | BedType | str | None = None
    numberOfRooms: QuantitativeValue | float | None = None
    occupancy: QuantitativeValue | None = None


@dataclass
class CampingPitch(Accommodation):
    pass


@dataclass
class Room(Accommodation):
    pass


@dataclass
class MusicRecording(CreativeWork):
    byArtist: MusicGroup | Person | None = None
    duration: Duration | None = None
    inAlbum: MusicAlbum | None = None
    inPlaylist: MusicPlaylist | None = None
    isrcCode: str | None = None
    recordingOf: MusicComposition | None = None


@dataclass
class ParcelDelivery(Intangible):
    carrier: Organization | None = None
    deliveryAddress: PostalAddress | None = None
    deliveryStatus: DeliveryEvent | None = None
    expectedArrivalFrom: datetime.date | datetime.datetime | None = None
    expectedArrivalUntil: datetime.date | datetime.datetime | None = None
    hasDeliveryMethod: DeliveryMethod | None = None
    itemShipped: Product | None = None
    originAddress: PostalAddress | None = None
    partOfOrder: Order | None = None
    provider: Organization | Person | None = None
    trackingNumber: str | None = None
    trackingUrl: URL | None = None


@dataclass
class Book(CreativeWork):
    abridged: bool | None = None
    bookEdition: str | None = None
    bookFormat: BookFormatType | None = None
    illustrator: Person | None = None
    isbn: str | None = None
    numberOfPages: Integer | None = None


@dataclass
class Dataset(CreativeWork):
    catalog: DataCatalog | None = None
    datasetTimeInterval: datetime.datetime | None = None
    distribution: DataDownload | None = None
    includedDataCatalog: DataCatalog | None = None
    includedInDataCatalog: DataCatalog | None = None
    issn: str | None = None
    measurementTechnique: URL | str | None = None
    variableMeasured: PropertyValue | str | None = None
    variablesMeasured: PropertyValue | str | None = None


@dataclass
class DataFeed(Dataset):
    dataFeedElement: DataFeedItem | Thing | str | None = None


@dataclass
class MediaObject(CreativeWork):
    associatedArticle: NewsArticle | None = None
    bitrate: str | None = None
    contentSize: str | None = None
    contentUrl: URL | None = None
    duration: Duration | None = None
    embedUrl: URL | None = None
    encodesCreativeWork: CreativeWork | None = None
    encodingFormat: URL | str | None = None
    endTime: datetime.datetime | datetime.time | None = None
    height: Distance | QuantitativeValue | None = None
    ineligibleRegion: GeoShape | Place | str | None = None
    interpretedAsClaim: Claim | None = None
    playerType: str | None = None
    productionCompany: Organization | None = None
    regionsAllowed: Place | None = None
    requiresSubscription: MediaSubscription | bool | None = None
    sha256: str | None = None
    startTime: datetime.datetime | datetime.time | None = None
    uploadDate: datetime.date | None = None
    width: Distance | QuantitativeValue | None = None


@dataclass
class AudioObject(MediaObject):
    caption: MediaObject | str | None = None
    embeddedTextCaption: str | None = None
    transcript: str | None = None


@dataclass
class ImageObject(MediaObject):
    caption: MediaObject | str | None = None
    embeddedTextCaption: str | None = None
    exifData: PropertyValue | str | None = None
    representativeOfPage: bool | None = None
    thumbnail: ImageObject | None = None


@dataclass
class VideoObject(MediaObject):
    actor: Person | None = None
    actors: Person | None = None
    caption: MediaObject | str | None = None
    director: Person | None = None
    directors: Person | None = None
    embeddedTextCaption: str | None = None
    musicBy: MusicGroup | Person | None = None
    thumbnail: ImageObject | None = None
    transcript: str | None = None
    videoFrameSize: str | None = None
    videoQuality: str | None = None


@dataclass
class d_3DModel(MediaObject):
    isResizable: bool | None = None


@dataclass
class MusicVideoObject(MediaObject):
    pass


@dataclass
class DataDownload(MediaObject):
    measurementTechnique: URL | str | None = None


@dataclass
class AmpStory(MediaObject):
    pass


@dataclass
class FundingScheme(Organization):
    pass


@dataclass
class JobPosting(Intangible):
    applicantLocationRequirements: AdministrativeArea | None = None
    applicationContact: ContactPoint | None = None
    baseSalary: MonetaryAmount | PriceSpecification | float | None = None
    benefits: str | None = None
    datePosted: datetime.date | datetime.datetime | None = None
    directApply: bool | None = None
    educationRequirements: EducationalOccupationalCredential | str | None = None
    eligibilityToWorkRequirement: str | None = None
    employerOverview: str | None = None
    employmentType: str | None = None
    employmentUnit: Organization | None = None
    estimatedSalary: MonetaryAmount | MonetaryAmountDistribution | float | None = None
    experienceInPlaceOfEducation: bool | None = None
    experienceRequirements: OccupationalExperienceRequirements | str | None = None
    hiringOrganization: Organization | None = None
    incentiveCompensation: str | None = None
    incentives: str | None = None
    industry: DefinedTerm | str | None = None
    jobBenefits: str | None = None
    jobImmediateStart: bool | None = None
    jobLocation: Place | None = None
    jobLocationType: str | None = None
    jobStartDate: datetime.date | str | None = None
    occupationalCategory: CategoryCode | str | None = None
    physicalRequirement: DefinedTerm | URL | str | None = None
    qualifications: EducationalOccupationalCredential | str | None = None
    relevantOccupation: Occupation | None = None
    responsibilities: str | None = None
    salaryCurrency: str | None = None
    securityClearanceRequirement: URL | str | None = None
    sensoryRequirement: DefinedTerm | URL | str | None = None
    skills: DefinedTerm | str | None = None
    specialCommitments: str | None = None
    title: str | None = None
    totalJobOpenings: Integer | None = None
    validThrough: datetime.date | datetime.datetime | None = None
    workHours: str | None = None


@dataclass
class MedicalOrganization(Organization):
    healthPlanNetworkId: str | None = None
    isAcceptingNewPatients: bool | None = None
    medicalSpecialty: MedicalSpecialty | None = None


@dataclass
class DiagnosticLab(MedicalOrganization):
    availableTest: MedicalTest | None = None


@dataclass
class VeterinaryCare(MedicalOrganization):
    pass


@dataclass
class MedicalProcedure(MedicalEntity):
    bodyLocation: str | None = None
    followup: str | None = None
    howPerformed: str | None = None
    preparation: MedicalEntity | str | None = None
    procedureType: MedicalProcedureType | None = None
    status: EventStatusType | MedicalStudyStatus | str | None = None


@dataclass
class TherapeuticProcedure(MedicalProcedure):
    adverseOutcome: MedicalEntity | None = None
    doseSchedule: DoseSchedule | None = None
    drug: Drug | None = None


@dataclass
class SurgicalProcedure(MedicalProcedure):
    pass


@dataclass
class DiagnosticProcedure(MedicalProcedure):
    pass


@dataclass
class SoftwareApplication(CreativeWork):
    applicationCategory: URL | str | None = None
    applicationSubCategory: URL | str | None = None
    applicationSuite: str | None = None
    availableOnDevice: str | None = None
    countriesNotSupported: str | None = None
    countriesSupported: str | None = None
    device: str | None = None
    downloadUrl: URL | None = None
    featureList: URL | str | None = None
    fileSize: str | None = None
    installUrl: URL | None = None
    memoryRequirements: URL | str | None = None
    operatingSystem: str | None = None
    permissions: str | None = None
    processorRequirements: str | None = None
    releaseNotes: URL | str | None = None
    requirements: URL | str | None = None
    screenshot: ImageObject | URL | None = None
    softwareAddOn: SoftwareApplication | None = None
    softwareHelp: CreativeWork | None = None
    softwareRequirements: URL | str | None = None
    softwareVersion: str | None = None
    storageRequirements: URL | str | None = None
    supportingData: DataFeed | None = None


@dataclass
class WebApplication(SoftwareApplication):
    browserRequirements: str | None = None


@dataclass
class MobileApplication(SoftwareApplication):
    carrierRequirements: str | None = None


@dataclass
class MerchantReturnPolicy(Intangible):
    additionalProperty: PropertyValue | None = None
    applicableCountry: Country | str | None = None
    customerRemorseReturnFees: ReturnFeesEnumeration | None = None
    customerRemorseReturnLabelSource: ReturnLabelSourceEnumeration | None = None
    customerRemorseReturnShippingFeesAmount: MonetaryAmount | None = None
    inStoreReturnsOffered: bool | None = None
    itemCondition: OfferItemCondition | None = None
    itemDefectReturnFees: ReturnFeesEnumeration | None = None
    itemDefectReturnLabelSource: ReturnLabelSourceEnumeration | None = None
    itemDefectReturnShippingFeesAmount: MonetaryAmount | None = None
    merchantReturnDays: Integer | datetime.date | datetime.datetime | None = None
    merchantReturnLink: URL | None = None
    refundType: RefundTypeEnumeration | None = None
    restockingFee: MonetaryAmount | float | None = None
    returnFees: ReturnFeesEnumeration | None = None
    returnLabelSource: ReturnLabelSourceEnumeration | None = None
    returnMethod: ReturnMethodEnumeration | None = None
    returnPolicyCategory: MerchantReturnEnumeration | None = None
    returnPolicyCountry: Country | str | None = None
    returnPolicySeasonalOverride: MerchantReturnPolicySeasonalOverride | None = None
    returnShippingFeesAmount: MonetaryAmount | None = None


@dataclass
class MerchantReturnPolicySeasonalOverride(Intangible):
    endDate: datetime.date | datetime.datetime | None = None
    merchantReturnDays: Integer | datetime.date | datetime.datetime | None = None
    returnPolicyCategory: MerchantReturnEnumeration | None = None
    startDate: datetime.date | datetime.datetime | None = None


@dataclass
class WebPage(CreativeWork):
    breadcrumb: BreadcrumbList | str | None = None
    lastReviewed: datetime.date | None = None
    mainContentOfPage: WebPageElement | None = None
    primaryImageOfPage: ImageObject | None = None
    relatedLink: URL | None = None
    reviewedBy: Organization | Person | None = None
    significantLink: URL | None = None
    significantLinks: URL | None = None
    speakable: SpeakableSpecification | URL | None = None
    specialty: Specialty | None = None


@dataclass
class AboutPage(WebPage):
    pass


@dataclass
class SearchResultsPage(WebPage):
    pass


@dataclass
class ContactPage(WebPage):
    pass


@dataclass
class CheckoutPage(WebPage):
    pass


@dataclass
class RealEstateListing(WebPage):
    datePosted: datetime.date | datetime.datetime | None = None
    leaseLength: Duration | QuantitativeValue | None = None


@dataclass
class FAQPage(WebPage):
    pass


@dataclass
class QAPage(WebPage):
    pass


@dataclass
class CollectionPage(WebPage):
    pass


@dataclass
class ProfilePage(WebPage):
    pass


@dataclass
class MedicalWebPage(WebPage):
    aspect: str | None = None
    medicalAudience: MedicalAudience | MedicalAudienceType | None = None


@dataclass
class ItemPage(WebPage):
    pass


@dataclass
class Festival(Event):
    pass


@dataclass
class Invoice(Intangible):
    accountId: str | None = None
    billingPeriod: Duration | None = None
    broker: Organization | Person | None = None
    category: CategoryCode | PhysicalActivityCategory | Thing | URL | str | None = None
    confirmationNumber: str | None = None
    customer: Organization | Person | None = None
    minimumPaymentDue: MonetaryAmount | PriceSpecification | None = None
    paymentDue: datetime.datetime | None = None
    paymentDueDate: datetime.date | datetime.datetime | None = None
    paymentMethod: PaymentMethod | None = None
    paymentMethodId: str | None = None
    paymentStatus: PaymentStatusType | str | None = None
    provider: Organization | Person | None = None
    referencesOrder: Order | None = None
    scheduledPaymentDate: datetime.date | None = None
    totalPaymentDue: MonetaryAmount | PriceSpecification | None = None


@dataclass
class HealthPlanNetwork(Intangible):
    healthPlanCostSharing: bool | None = None
    healthPlanNetworkId: str | None = None
    healthPlanNetworkTier: str | None = None


@dataclass
class SportsEvent(Event):
    awayTeam: Person | SportsTeam | None = None
    competitor: Person | SportsTeam | None = None
    homeTeam: Person | SportsTeam | None = None
    sport: URL | str | None = None


@dataclass
class ProductReturnPolicy(Intangible):
    productReturnDays: Integer | None = None
    productReturnLink: URL | None = None


@dataclass
class EnergyConsumptionDetails(Intangible):
    energyEfficiencyScaleMax: EUEnergyEfficiencyEnumeration | None = None
    energyEfficiencyScaleMin: EUEnergyEfficiencyEnumeration | None = None
    hasEnergyEfficiencyCategory: EnergyEfficiencyEnumeration | None = None


@dataclass
class HealthPlanCostSharingSpecification(Intangible):
    healthPlanCoinsuranceOption: str | None = None
    healthPlanCoinsuranceRate: float | None = None
    healthPlanCopay: PriceSpecification | None = None
    healthPlanCopayOption: str | None = None
    healthPlanPharmacyCategory: str | None = None


@dataclass
class EducationEvent(Event):
    assesses: DefinedTerm | str | None = None
    educationalLevel: DefinedTerm | URL | str | None = None
    teaches: DefinedTerm | str | None = None


@dataclass
class LearningResource(CreativeWork):
    assesses: DefinedTerm | str | None = None
    competencyRequired: DefinedTerm | URL | str | None = None
    educationalAlignment: AlignmentObject | None = None
    educationalLevel: DefinedTerm | URL | str | None = None
    educationalUse: DefinedTerm | str | None = None
    learningResourceType: DefinedTerm | str | None = None
    teaches: DefinedTerm | str | None = None


@dataclass
class Course(LearningResource):
    courseCode: str | None = None
    coursePrerequisites: AlignmentObject | Course | str | None = None
    educationalCredentialAwarded: EducationalOccupationalCredential | URL | str | None = None
    hasCourseInstance: CourseInstance | None = None
    numberOfCredits: Integer | StructuredValue | None = None
    occupationalCredentialAwarded: EducationalOccupationalCredential | URL | str | None = None


@dataclass
class Quiz(LearningResource):
    pass


@dataclass
class PlayAction(Action):
    audience: Audience | None = None
    event: Event | None = None


@dataclass
class PerformAction(PlayAction):
    entertainmentBusiness: EntertainmentBusiness | None = None


@dataclass
class ExerciseAction(PlayAction):
    course: Place | None = None
    diet: Diet | None = None
    distance: Distance | None = None
    exerciseCourse: Place | None = None
    exercisePlan: ExercisePlan | None = None
    exerciseRelatedDiet: Diet | None = None
    exerciseType: str | None = None
    fromLocation: Place | None = None
    opponent: Person | None = None
    sportsActivityLocation: SportsActivityLocation | None = None
    sportsEvent: SportsEvent | None = None
    sportsTeam: SportsTeam | None = None
    toLocation: Place | None = None


@dataclass
class Reservation(Intangible):
    bookingAgent: Organization | Person | None = None
    bookingTime: datetime.datetime | None = None
    broker: Organization | Person | None = None
    modifiedTime: datetime.datetime | None = None
    priceCurrency: str | None = None
    programMembershipUsed: ProgramMembership | None = None
    provider: Organization | Person | None = None
    reservationFor: Thing | None = None
    reservationId: str | None = None
    reservationStatus: ReservationStatusType | None = None
    reservedTicket: Ticket | None = None
    totalPrice: PriceSpecification | float | str | None = None
    underName: Organization | Person | None = None


@dataclass
class FlightReservation(Reservation):
    boardingGroup: str | None = None
    passengerPriorityStatus: QualitativeValue | str | None = None
    passengerSequenceNumber: str | None = None
    securityScreening: str | None = None


@dataclass
class LodgingReservation(Reservation):
    checkinTime: datetime.datetime | datetime.time | None = None
    checkoutTime: datetime.datetime | datetime.time | None = None
    lodgingUnitDescription: str | None = None
    lodgingUnitType: QualitativeValue | str | None = None
    numAdults: Integer | QuantitativeValue | None = None
    numChildren: Integer | QuantitativeValue | None = None


@dataclass
class BoatReservation(Reservation):
    pass


@dataclass
class TaxiReservation(Reservation):
    partySize: Integer | QuantitativeValue | None = None
    pickupLocation: Place | None = None
    pickupTime: datetime.datetime | None = None


@dataclass
class FoodEstablishmentReservation(Reservation):
    endTime: datetime.datetime | datetime.time | None = None
    partySize: Integer | QuantitativeValue | None = None
    startTime: datetime.datetime | datetime.time | None = None


@dataclass
class BusReservation(Reservation):
    pass


@dataclass
class ReservationPackage(Reservation):
    subReservation: Reservation | None = None


@dataclass
class RentalCarReservation(Reservation):
    dropoffLocation: Place | None = None
    dropoffTime: datetime.datetime | None = None
    pickupLocation: Place | None = None
    pickupTime: datetime.datetime | None = None


@dataclass
class TrainReservation(Reservation):
    pass


@dataclass
class EventReservation(Reservation):
    pass


@dataclass
class Vehicle(Product):
    accelerationTime: QuantitativeValue | None = None
    bodyType: QualitativeValue | URL | str | None = None
    callSign: str | None = None
    cargoVolume: QuantitativeValue | None = None
    dateVehicleFirstRegistered: datetime.date | None = None
    driveWheelConfiguration: DriveWheelConfigurationValue | str | None = None
    emissionsCO2: float | None = None
    fuelCapacity: QuantitativeValue | None = None
    fuelConsumption: QuantitativeValue | None = None
    fuelEfficiency: QuantitativeValue | None = None
    fuelType: QualitativeValue | URL | str | None = None
    knownVehicleDamages: str | None = None
    meetsEmissionStandard: QualitativeValue | URL | str | None = None
    mileageFromOdometer: QuantitativeValue | None = None
    modelDate: datetime.date | None = None
    numberOfAirbags: float | str | None = None
    numberOfAxles: QuantitativeValue | float | None = None
    numberOfDoors: QuantitativeValue | float | None = None
    numberOfForwardGears: QuantitativeValue | float | None = None
    numberOfPreviousOwners: QuantitativeValue | float | None = None
    payload: QuantitativeValue | None = None
    productionDate: datetime.date | None = None
    purchaseDate: datetime.date | None = None
    seatingCapacity: QuantitativeValue | float | None = None
    speed: QuantitativeValue | None = None
    steeringPosition: SteeringPositionValue | None = None
    stupidProperty: QuantitativeValue | None = None
    tongueWeight: QuantitativeValue | None = None
    trailerWeight: QuantitativeValue | None = None
    vehicleConfiguration: str | None = None
    vehicleEngine: EngineSpecification | None = None
    vehicleIdentificationNumber: str | None = None
    vehicleInteriorColor: str | None = None
    vehicleInteriorType: str | None = None
    vehicleModelDate: datetime.date | None = None
    vehicleSeatingCapacity: QuantitativeValue | float | None = None
    vehicleSpecialUsage: CarUsageType | str | None = None
    vehicleTransmission: QualitativeValue | URL | str | None = None
    weightTotal: QuantitativeValue | None = None
    wheelbase: QuantitativeValue | None = None


@dataclass
class Car(Vehicle):
    acrissCode: str | None = None
    roofLoad: QuantitativeValue | None = None


@dataclass
class BusOrCoach(Vehicle):
    acrissCode: str | None = None
    roofLoad: QuantitativeValue | None = None


@dataclass
class MotorizedBicycle(Vehicle):
    pass


@dataclass
class Motorcycle(Vehicle):
    pass


@dataclass
class EducationalOccupationalProgram(Intangible):
    applicationDeadline: datetime.date | None = None
    applicationStartDate: datetime.date | None = None
    dayOfWeek: DayOfWeek | None = None
    educationalCredentialAwarded: EducationalOccupationalCredential | URL | str | None = None
    educationalProgramMode: URL | str | None = None
    endDate: datetime.date | datetime.datetime | None = None
    financialAidEligible: DefinedTerm | str | None = None
    hasCourse: Course | None = None
    maximumEnrollment: Integer | None = None
    numberOfCredits: Integer | StructuredValue | None = None
    occupationalCategory: CategoryCode | str | None = None
    occupationalCredentialAwarded: EducationalOccupationalCredential | URL | str | None = None
    offers: Demand | Offer | None = None
    programPrerequisites: AlignmentObject | Course | EducationalOccupationalCredential | str | None = None
    programType: DefinedTerm | str | None = None
    provider: Organization | Person | None = None
    salaryUponCompletion: MonetaryAmountDistribution | None = None
    startDate: datetime.date | datetime.datetime | None = None
    termDuration: Duration | None = None
    termsPerYear: float | None = None
    timeOfDay: str | None = None
    timeToComplete: Duration | None = None
    trainingSalary: MonetaryAmountDistribution | None = None
    typicalCreditsPerTerm: Integer | StructuredValue | None = None


@dataclass
class WorkBasedProgram(EducationalOccupationalProgram):
    occupationalCategory: CategoryCode | str | None = None
    trainingSalary: MonetaryAmountDistribution | None = None


@dataclass
class EducationalOccupationalCredential(CreativeWork):
    competencyRequired: DefinedTerm | URL | str | None = None
    credentialCategory: DefinedTerm | URL | str | None = None
    educationalLevel: DefinedTerm | URL | str | None = None
    recognizedBy: Organization | None = None
    validFor: Duration | None = None
    validIn: AdministrativeArea | None = None


@dataclass
class Offer(Intangible):
    acceptedPaymentMethod: LoanOrCredit | PaymentMethod | None = None
    addOn: Offer | None = None
    advanceBookingRequirement: QuantitativeValue | None = None
    aggregateRating: AggregateRating | None = None
    areaServed: AdministrativeArea | GeoShape | Place | str | None = None
    availability: ItemAvailability | None = None
    availabilityEnds: datetime.date | datetime.datetime | datetime.time | None = None
    availabilityStarts: datetime.date | datetime.datetime | datetime.time | None = None
    availableAtOrFrom: Place | None = None
    availableDeliveryMethod: DeliveryMethod | None = None
    businessFunction: BusinessFunction | None = None
    category: CategoryCode | PhysicalActivityCategory | Thing | URL | str | None = None
    deliveryLeadTime: QuantitativeValue | None = None
    eligibleCustomerType: BusinessEntityType | None = None
    eligibleDuration: QuantitativeValue | None = None
    eligibleQuantity: QuantitativeValue | None = None
    eligibleRegion: GeoShape | Place | str | None = None
    eligibleTransactionVolume: PriceSpecification | None = None
    gtin: str | None = None
    gtin12: str | None = None
    gtin13: str | None = None
    gtin14: str | None = None
    gtin8: str | None = None
    hasAdultConsideration: AdultOrientedEnumeration | None = None
    hasMeasurement: QuantitativeValue | None = None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None = None
    includesObject: TypeAndQuantityNode | None = None
    ineligibleRegion: GeoShape | Place | str | None = None
    inventoryLevel: QuantitativeValue | None = None
    isFamilyFriendly: bool | None = None
    itemCondition: OfferItemCondition | None = None
    itemOffered: AggregateOffer | CreativeWork | Event | MenuItem | Product | Service | Trip | None = None
    leaseLength: Duration | QuantitativeValue | None = None
    mpn: str | None = None
    offeredBy: Organization | Person | None = None
    price: float | str | None = None
    priceCurrency: str | None = None
    priceSpecification: PriceSpecification | None = None
    priceValidUntil: datetime.date | None = None
    review: Review | None = None
    reviews: Review | None = None
    seller: Organization | Person | None = None
    serialNumber: str | None = None
    shippingDetails: OfferShippingDetails | None = None
    sku: str | None = None
    validFrom: datetime.date | datetime.datetime | None = None
    validThrough: datetime.date | datetime.datetime | None = None
    warranty: WarrantyPromise | None = None


@dataclass
class OfferForLease(Offer):
    pass


@dataclass
class AggregateOffer(Offer):
    highPrice: float | str | None = None
    lowPrice: float | str | None = None
    offerCount: Integer | None = None
    offers: Demand | Offer | None = None


@dataclass
class OfferForPurchase(Offer):
    pass


@dataclass
class Permit(Intangible):
    issuedBy: Organization | None = None
    issuedThrough: Service | None = None
    permitAudience: Audience | None = None
    validFor: Duration | None = None
    validFrom: datetime.date | datetime.datetime | None = None
    validIn: AdministrativeArea | None = None
    validUntil: datetime.date | None = None


@dataclass
class GovernmentPermit(Permit):
    pass


@dataclass
class SoftwareSourceCode(CreativeWork):
    codeRepository: URL | None = None
    codeSampleType: str | None = None
    programmingLanguage: ComputerLanguage | str | None = None
    runtime: str | None = None
    runtimePlatform: str | None = None
    sampleType: str | None = None
    targetProduct: SoftwareApplication | None = None


@dataclass
class Brand(Intangible):
    aggregateRating: AggregateRating | None = None
    logo: ImageObject | URL | None = None
    review: Review | None = None
    slogan: str | None = None


@dataclass
class Occupation(Intangible):
    educationRequirements: EducationalOccupationalCredential | str | None = None
    estimatedSalary: MonetaryAmount | MonetaryAmountDistribution | float | None = None
    experienceRequirements: OccupationalExperienceRequirements | str | None = None
    occupationLocation: AdministrativeArea | None = None
    occupationalCategory: CategoryCode | str | None = None
    qualifications: EducationalOccupationalCredential | str | None = None
    responsibilities: str | None = None
    skills: DefinedTerm | str | None = None


@dataclass
class HowTo(CreativeWork):
    estimatedCost: MonetaryAmount | str | None = None
    performTime: Duration | None = None
    prepTime: Duration | None = None
    step: CreativeWork | HowToSection | HowToStep | str | None = None
    steps: CreativeWork | ItemList | str | None = None
    supply: HowToSupply | str | None = None
    tool: HowToTool | str | None = None
    totalTime: Duration | None = None
    yield_: QuantitativeValue | str | None = None


@dataclass
class Recipe(HowTo):
    cookTime: Duration | None = None
    cookingMethod: str | None = None
    ingredients: str | None = None
    nutrition: NutritionInformation | None = None
    recipeCategory: str | None = None
    recipeCuisine: str | None = None
    recipeIngredient: str | None = None
    recipeInstructions: CreativeWork | ItemList | str | None = None
    recipeYield: QuantitativeValue | str | None = None
    suitableForDiet: RestrictedDiet | None = None


@dataclass
class ActionAccessSpecification(Intangible):
    availabilityEnds: datetime.date | datetime.datetime | datetime.time | None = None
    availabilityStarts: datetime.date | datetime.datetime | datetime.time | None = None
    category: CategoryCode | PhysicalActivityCategory | Thing | URL | str | None = None
    eligibleRegion: GeoShape | Place | str | None = None
    expectsAcceptanceOf: Offer | None = None
    ineligibleRegion: GeoShape | Place | str | None = None
    requiresSubscription: MediaSubscription | bool | None = None


@dataclass
class ConsumeAction(Action):
    actionAccessibilityRequirement: ActionAccessSpecification | None = None
    expectsAcceptanceOf: Offer | None = None


@dataclass
class PlayGameAction(ConsumeAction):
    gameAvailabilityType: GameAvailabilityEnumeration | str | None = None


@dataclass
class ReadAction(ConsumeAction):
    pass


@dataclass
class ListenAction(ConsumeAction):
    pass


@dataclass
class ViewAction(ConsumeAction):
    pass


@dataclass
class EatAction(ConsumeAction):
    pass


@dataclass
class UseAction(ConsumeAction):
    pass


@dataclass
class DrinkAction(ConsumeAction):
    pass


@dataclass
class InstallAction(ConsumeAction):
    pass


@dataclass
class WatchAction(ConsumeAction):
    pass


@dataclass
class MediaSubscription(Intangible):
    authenticator: Organization | None = None
    expectsAcceptanceOf: Offer | None = None


@dataclass
class NewsMediaOrganization(Organization):
    actionableFeedbackPolicy: CreativeWork | URL | None = None
    correctionsPolicy: CreativeWork | URL | None = None
    diversityPolicy: CreativeWork | URL | None = None
    diversityStaffingReport: Article | URL | None = None
    ethicsPolicy: CreativeWork | URL | None = None
    masthead: CreativeWork | URL | None = None
    missionCoveragePrioritiesPolicy: CreativeWork | URL | None = None
    noBylinesPolicy: CreativeWork | URL | None = None
    ownershipFundingInfo: AboutPage | CreativeWork | URL | str | None = None
    unnamedSourcesPolicy: CreativeWork | URL | None = None
    verificationFactCheckingPolicy: CreativeWork | URL | None = None


@dataclass
class Ticket(Intangible):
    dateIssued: datetime.date | datetime.datetime | None = None
    issuedBy: Organization | None = None
    priceCurrency: str | None = None
    ticketNumber: str | None = None
    ticketToken: URL | str | None = None
    ticketedSeat: Seat | None = None
    totalPrice: PriceSpecification | float | str | None = None
    underName: Organization | Person | None = None


@dataclass
class Message(CreativeWork):
    bccRecipient: ContactPoint | Organization | Person | None = None
    ccRecipient: ContactPoint | Organization | Person | None = None
    dateRead: datetime.date | datetime.datetime | None = None
    dateReceived: datetime.datetime | None = None
    dateSent: datetime.datetime | None = None
    messageAttachment: CreativeWork | None = None
    recipient: Audience | ContactPoint | Organization | Person | None = None
    sender: Audience | Organization | Person | None = None
    toRecipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class EmailMessage(Message):
    pass


@dataclass
class Demand(Intangible):
    acceptedPaymentMethod: LoanOrCredit | PaymentMethod | None = None
    advanceBookingRequirement: QuantitativeValue | None = None
    areaServed: AdministrativeArea | GeoShape | Place | str | None = None
    availability: ItemAvailability | None = None
    availabilityEnds: datetime.date | datetime.datetime | datetime.time | None = None
    availabilityStarts: datetime.date | datetime.datetime | datetime.time | None = None
    availableAtOrFrom: Place | None = None
    availableDeliveryMethod: DeliveryMethod | None = None
    businessFunction: BusinessFunction | None = None
    deliveryLeadTime: QuantitativeValue | None = None
    eligibleCustomerType: BusinessEntityType | None = None
    eligibleDuration: QuantitativeValue | None = None
    eligibleQuantity: QuantitativeValue | None = None
    eligibleRegion: GeoShape | Place | str | None = None
    eligibleTransactionVolume: PriceSpecification | None = None
    gtin: str | None = None
    gtin12: str | None = None
    gtin13: str | None = None
    gtin14: str | None = None
    gtin8: str | None = None
    includesObject: TypeAndQuantityNode | None = None
    ineligibleRegion: GeoShape | Place | str | None = None
    inventoryLevel: QuantitativeValue | None = None
    itemCondition: OfferItemCondition | None = None
    itemOffered: AggregateOffer | CreativeWork | Event | MenuItem | Product | Service | Trip | None = None
    mpn: str | None = None
    priceSpecification: PriceSpecification | None = None
    seller: Organization | Person | None = None
    serialNumber: str | None = None
    sku: str | None = None
    validFrom: datetime.date | datetime.datetime | None = None
    validThrough: datetime.date | datetime.datetime | None = None
    warranty: WarrantyPromise | None = None


@dataclass
class Schedule(Intangible):
    byDay: DayOfWeek | str | None = None
    byMonth: Integer | None = None
    byMonthDay: Integer | None = None
    byMonthWeek: Integer | None = None
    duration: Duration | None = None
    endDate: datetime.date | datetime.datetime | None = None
    endTime: datetime.datetime | datetime.time | None = None
    exceptDate: datetime.date | datetime.datetime | None = None
    repeatCount: Integer | None = None
    repeatFrequency: Duration | str | None = None
    scheduleTimezone: str | None = None
    startDate: datetime.date | datetime.datetime | None = None
    startTime: datetime.datetime | datetime.time | None = None


@dataclass
class MedicalGuideline(MedicalEntity):
    evidenceLevel: MedicalEvidenceLevel | None = None
    evidenceOrigin: str | None = None
    guidelineDate: datetime.date | None = None
    guidelineSubject: MedicalEntity | None = None


@dataclass
class MedicalGuidelineContraindication(MedicalGuideline):
    pass


@dataclass
class MedicalGuidelineRecommendation(MedicalGuideline):
    recommendationStrength: str | None = None


@dataclass
class Airline(Organization):
    boardingPolicy: BoardingPolicyType | None = None
    iataCode: str | None = None


@dataclass
class MathSolver(CreativeWork):
    mathExpression: SolveMathAction | str | None = None


@dataclass
class MusicComposition(CreativeWork):
    composer: Organization | Person | None = None
    firstPerformance: Event | None = None
    includedComposition: MusicComposition | None = None
    iswcCode: str | None = None
    lyricist: Person | None = None
    lyrics: CreativeWork | None = None
    musicArrangement: MusicComposition | None = None
    musicCompositionForm: str | None = None
    musicalKey: str | None = None
    recordedAs: MusicRecording | None = None


@dataclass
class GameServer(Intangible):
    game: VideoGame | None = None
    playersOnline: Integer | None = None
    serverStatus: GameServerStatus | None = None


@dataclass
class SpeakableSpecification(Intangible):
    cssSelector: CssSelectorType | None = None
    xpath: XPathType | None = None


@dataclass
class AlignmentObject(Intangible):
    alignmentType: str | None = None
    educationalFramework: str | None = None
    targetDescription: str | None = None
    targetName: str | None = None
    targetUrl: URL | None = None


@dataclass
class Drawing(CreativeWork):
    pass


@dataclass
class Order(Intangible):
    acceptedOffer: Offer | None = None
    billingAddress: PostalAddress | None = None
    broker: Organization | Person | None = None
    confirmationNumber: str | None = None
    customer: Organization | Person | None = None
    discount: float | str | None = None
    discountCode: str | None = None
    discountCurrency: str | None = None
    isGift: bool | None = None
    merchant: Organization | Person | None = None
    orderDate: datetime.date | datetime.datetime | None = None
    orderDelivery: ParcelDelivery | None = None
    orderNumber: str | None = None
    orderStatus: OrderStatus | None = None
    orderedItem: OrderItem | Product | Service | None = None
    partOfInvoice: Invoice | None = None
    paymentDue: datetime.datetime | None = None
    paymentDueDate: datetime.date | datetime.datetime | None = None
    paymentMethod: PaymentMethod | None = None
    paymentMethodId: str | None = None
    paymentUrl: URL | None = None
    seller: Organization | Person | None = None


@dataclass
class OrderItem(Intangible):
    orderDelivery: ParcelDelivery | None = None
    orderItemNumber: str | None = None
    orderItemStatus: OrderStatus | None = None
    orderQuantity: float | None = None
    orderedItem: OrderItem | Product | Service | None = None


@dataclass
class MedicalDevice(MedicalEntity):
    adverseOutcome: MedicalEntity | None = None
    contraindication: MedicalContraindication | str | None = None
    postOp: str | None = None
    preOp: str | None = None
    procedure: str | None = None
    seriousAdverseOutcome: MedicalEntity | None = None


@dataclass
class AnatomicalStructure(MedicalEntity):
    associatedPathophysiology: str | None = None
    bodyLocation: str | None = None
    connectedTo: AnatomicalStructure | None = None
    diagram: ImageObject | None = None
    partOfSystem: AnatomicalSystem | None = None
    relatedCondition: MedicalCondition | None = None
    relatedTherapy: MedicalTherapy | None = None
    subStructure: AnatomicalStructure | None = None


@dataclass
class Nerve(AnatomicalStructure):
    branch: AnatomicalStructure | None = None
    nerveMotor: Muscle | None = None
    sensoryUnit: AnatomicalStructure | SuperficialAnatomy | None = None
    sourcedFrom: BrainStructure | None = None


@dataclass
class Muscle(AnatomicalStructure):
    antagonist: Muscle | None = None
    bloodSupply: Vessel | None = None
    insertion: AnatomicalStructure | None = None
    muscleAction: str | None = None
    nerve: Nerve | None = None


@dataclass
class Vessel(AnatomicalStructure):
    pass


@dataclass
class Joint(AnatomicalStructure):
    biomechnicalClass: str | None = None
    functionalClass: MedicalEntity | str | None = None
    structuralClass: str | None = None


@dataclass
class Bone(AnatomicalStructure):
    pass


@dataclass
class Ligament(AnatomicalStructure):
    pass


@dataclass
class BrainStructure(AnatomicalStructure):
    pass


@dataclass
class Review(CreativeWork):
    associatedClaimReview: Review | None = None
    associatedMediaReview: Review | None = None
    associatedReview: Review | None = None
    itemReviewed: Thing | None = None
    negativeNotes: ItemList | ListItem | WebContent | str | None = None
    positiveNotes: ItemList | ListItem | WebContent | str | None = None
    reviewAspect: str | None = None
    reviewBody: str | None = None
    reviewRating: Rating | None = None


@dataclass
class MediaReview(Review):
    mediaAuthenticityCategory: MediaManipulationRatingEnumeration | None = None
    originalMediaContextDescription: str | None = None
    originalMediaLink: MediaObject | URL | WebPage | None = None


@dataclass
class Recommendation(Review):
    category: CategoryCode | PhysicalActivityCategory | Thing | URL | str | None = None


@dataclass
class CriticReview(Review):
    pass


@dataclass
class ClaimReview(Review):
    claimReviewed: str | None = None


@dataclass
class EmployerReview(Review):
    pass


@dataclass
class UserReview(Review):
    pass


@dataclass
class ProgramMembership(Intangible):
    hostingOrganization: Organization | None = None
    member: Organization | Person | None = None
    members: Organization | Person | None = None
    membershipNumber: str | None = None
    membershipPointsEarned: QuantitativeValue | float | None = None
    programName: str | None = None


@dataclass
class ServiceChannel(Intangible):
    availableLanguage: Language | str | None = None
    processingTime: Duration | None = None
    providesService: Service | None = None
    serviceLocation: Place | None = None
    servicePhone: ContactPoint | None = None
    servicePostalAddress: PostalAddress | None = None
    serviceSmsNumber: ContactPoint | None = None
    serviceUrl: URL | None = None


@dataclass
class Role(Intangible):
    endDate: datetime.date | datetime.datetime | None = None
    namedPosition: URL | str | None = None
    roleName: URL | str | None = None
    startDate: datetime.date | datetime.datetime | None = None


@dataclass
class PerformanceRole(Role):
    characterName: str | None = None


@dataclass
class OrganizationRole(Role):
    numberedPosition: float | None = None


@dataclass
class LinkRole(Role):
    inLanguage: Language | str | None = None
    linkRelationship: str | None = None


@dataclass
class NGO(Organization):
    pass


@dataclass
class Clip(CreativeWork):
    actor: Person | None = None
    actors: Person | None = None
    clipNumber: Integer | str | None = None
    director: Person | None = None
    directors: Person | None = None
    endOffset: HyperTocEntry | float | None = None
    musicBy: MusicGroup | Person | None = None
    partOfEpisode: Episode | None = None
    partOfSeason: CreativeWorkSeason | None = None
    partOfSeries: CreativeWorkSeries | None = None
    startOffset: HyperTocEntry | float | None = None


@dataclass
class MovieClip(Clip):
    pass


@dataclass
class VideoGameClip(Clip):
    pass


@dataclass
class TVClip(Clip):
    partOfTVSeries: TVSeries | None = None


@dataclass
class RadioClip(Clip):
    pass


@dataclass
class SeekToAction(Action):
    startOffset: HyperTocEntry | float | None = None


@dataclass
class MedicalCause(MedicalEntity):
    causeOf: MedicalEntity | None = None


@dataclass
class DrugCost(MedicalEntity):
    applicableLocation: AdministrativeArea | None = None
    costCategory: DrugCostCategory | None = None
    costCurrency: str | None = None
    costOrigin: str | None = None
    costPerUnit: QualitativeValue | float | str | None = None
    drugUnit: str | None = None


@dataclass
class MusicPlaylist(CreativeWork):
    numTracks: Integer | None = None
    track: ItemList | MusicRecording | None = None
    tracks: MusicRecording | None = None


@dataclass
class MusicRelease(MusicPlaylist):
    catalogNumber: str | None = None
    creditedTo: Organization | Person | None = None
    duration: Duration | None = None
    musicReleaseFormat: MusicReleaseFormatType | None = None
    recordLabel: Organization | None = None
    releaseOf: MusicAlbum | None = None


@dataclass
class MusicAlbum(MusicPlaylist):
    albumProductionType: MusicAlbumProductionType | None = None
    albumRelease: MusicRelease | None = None
    albumReleaseType: MusicAlbumReleaseType | None = None
    byArtist: MusicGroup | Person | None = None


@dataclass
class TouristAttraction(Place):
    availableLanguage: Language | str | None = None
    touristType: Audience | str | None = None


@dataclass
class TouristDestination(Place):
    includesAttraction: TouristAttraction | None = None
    touristType: Audience | str | None = None


@dataclass
class PropertyValueSpecification(Intangible):
    defaultValue: Thing | str | None = None
    maxValue: float | None = None
    minValue: float | None = None
    multipleValues: bool | None = None
    readonlyValue: bool | None = None
    stepValue: float | None = None
    valueMaxLength: float | None = None
    valueMinLength: float | None = None
    valueName: str | None = None
    valuePattern: str | None = None
    valueRequired: bool | None = None


@dataclass
class Service(Intangible):
    aggregateRating: AggregateRating | None = None
    areaServed: AdministrativeArea | GeoShape | Place | str | None = None
    audience: Audience | None = None
    availableChannel: ServiceChannel | None = None
    award: str | None = None
    brand: Brand | Organization | None = None
    broker: Organization | Person | None = None
    category: CategoryCode | PhysicalActivityCategory | Thing | URL | str | None = None
    hasOfferCatalog: OfferCatalog | None = None
    hoursAvailable: OpeningHoursSpecification | None = None
    isRelatedTo: Product | Service | None = None
    isSimilarTo: Product | Service | None = None
    logo: ImageObject | URL | None = None
    offers: Demand | Offer | None = None
    produces: Thing | None = None
    provider: Organization | Person | None = None
    providerMobility: str | None = None
    review: Review | None = None
    serviceArea: AdministrativeArea | GeoShape | Place | None = None
    serviceAudience: Audience | None = None
    serviceOutput: Thing | None = None
    serviceType: GovernmentBenefitsType | str | None = None
    slogan: str | None = None
    termsOfService: URL | str | None = None


@dataclass
class FinancialProduct(Service):
    annualPercentageRate: QuantitativeValue | float | None = None
    feesAndCommissionsSpecification: URL | str | None = None
    interestRate: QuantitativeValue | float | None = None


@dataclass
class CableOrSatelliteService(Service):
    pass


@dataclass
class TaxiService(Service):
    pass


@dataclass
class BroadcastService(Service):
    area: Place | None = None
    broadcastAffiliateOf: Organization | None = None
    broadcastDisplayName: str | None = None
    broadcastFrequency: BroadcastFrequencySpecification | str | None = None
    broadcastTimezone: str | None = None
    broadcaster: Organization | None = None
    callSign: str | None = None
    hasBroadcastChannel: BroadcastChannel | None = None
    inLanguage: Language | str | None = None
    parentService: BroadcastService | None = None
    videoFormat: str | None = None


@dataclass
class WebAPI(Service):
    documentation: CreativeWork | URL | None = None


@dataclass
class GovernmentService(Service):
    jurisdiction: AdministrativeArea | str | None = None
    serviceOperator: Organization | None = None


@dataclass
class FoodService(Service):
    pass


@dataclass
class Taxi(Service):
    pass


@dataclass
class ShortStory(CreativeWork):
    pass


@dataclass
class DeliveryEvent(Event):
    accessCode: str | None = None
    availableFrom: datetime.datetime | None = None
    availableThrough: datetime.datetime | None = None
    hasDeliveryMethod: DeliveryMethod | None = None


@dataclass
class CreativeWorkSeason(CreativeWork):
    actor: Person | None = None
    director: Person | None = None
    endDate: datetime.date | datetime.datetime | None = None
    episode: Episode | None = None
    episodes: Episode | None = None
    numberOfEpisodes: Integer | None = None
    partOfSeries: CreativeWorkSeries | None = None
    productionCompany: Organization | None = None
    seasonNumber: Integer | str | None = None
    startDate: datetime.date | datetime.datetime | None = None
    trailer: VideoObject | None = None


@dataclass
class TVSeason(CreativeWorkSeason):
    countryOfOrigin: Country | None = None
    partOfTVSeries: TVSeries | None = None


@dataclass
class RadioSeason(CreativeWorkSeason):
    pass


@dataclass
class PodcastSeason(CreativeWorkSeason):
    pass


@dataclass
class DanceEvent(Event):
    pass


@dataclass
class HealthPlanFormulary(Intangible):
    healthPlanCostSharing: bool | None = None
    healthPlanDrugTier: str | None = None
    offersPrescriptionByMail: bool | None = None


@dataclass
class Legislation(CreativeWork):
    jurisdiction: AdministrativeArea | str | None = None
    legislationApplies: Legislation | None = None
    legislationChanges: Legislation | None = None
    legislationConsolidates: Legislation | None = None
    legislationDate: datetime.date | None = None
    legislationDateVersion: datetime.date | None = None
    legislationIdentifier: URL | str | None = None
    legislationJurisdiction: AdministrativeArea | str | None = None
    legislationLegalForce: LegalForceStatus | None = None
    legislationPassedBy: Organization | Person | None = None
    legislationResponsible: Organization | Person | None = None
    legislationTransposes: Legislation | None = None
    legislationType: CategoryCode | str | None = None


@dataclass
class LegislationObject(Legislation, MediaObject):
    legislationLegalValue: LegalValueLevel | None = None


@dataclass
class DataFeedItem(Intangible):
    dateCreated: datetime.date | datetime.datetime | None = None
    dateDeleted: datetime.date | datetime.datetime | None = None
    dateModified: datetime.date | datetime.datetime | None = None
    item: Thing | None = None


@dataclass
class Corporation(Organization):
    tickerSymbol: str | None = None


@dataclass
class SocialEvent(Event):
    pass


@dataclass
class Episode(CreativeWork):
    actor: Person | None = None
    actors: Person | None = None
    director: Person | None = None
    directors: Person | None = None
    duration: Duration | None = None
    episodeNumber: Integer | str | None = None
    musicBy: MusicGroup | Person | None = None
    partOfSeason: CreativeWorkSeason | None = None
    partOfSeries: CreativeWorkSeries | None = None
    productionCompany: Organization | None = None
    trailer: VideoObject | None = None


@dataclass
class TVEpisode(Episode):
    countryOfOrigin: Country | None = None
    partOfTVSeries: TVSeries | None = None
    subtitleLanguage: Language | str | None = None
    titleEIDR: URL | str | None = None


@dataclass
class RadioEpisode(Episode):
    pass


@dataclass
class PodcastEpisode(Episode):
    pass


@dataclass
class VisualArtwork(CreativeWork):
    artEdition: Integer | str | None = None
    artMedium: URL | str | None = None
    artform: URL | str | None = None
    artist: Person | None = None
    artworkSurface: URL | str | None = None
    colorist: Person | None = None
    depth: Distance | QuantitativeValue | None = None
    height: Distance | QuantitativeValue | None = None
    inker: Person | None = None
    letterer: Person | None = None
    penciler: Person | None = None
    surface: URL | str | None = None
    width: Distance | QuantitativeValue | None = None


@dataclass
class CoverArt(VisualArtwork):
    pass


@dataclass
class ItemList(Intangible):
    itemListElement: ListItem | Thing | str | None = None
    itemListOrder: ItemListOrderType | str | None = None
    numberOfItems: Integer | None = None


@dataclass
class BreadcrumbList(ItemList):
    pass


@dataclass
class OfferCatalog(ItemList):
    pass


@dataclass
class SpecialAnnouncement(CreativeWork):
    announcementLocation: CivicStructure | LocalBusiness | None = None
    category: CategoryCode | PhysicalActivityCategory | Thing | URL | str | None = None
    datePosted: datetime.date | datetime.datetime | None = None
    diseasePreventionInfo: URL | WebContent | None = None
    diseaseSpreadStatistics: Dataset | Observation | URL | WebContent | None = None
    gettingTestedInfo: URL | WebContent | None = None
    governmentBenefitsInfo: GovernmentService | None = None
    newsUpdatesAndGuidelines: URL | WebContent | None = None
    publicTransportClosuresInfo: URL | WebContent | None = None
    quarantineGuidelines: URL | WebContent | None = None
    schoolClosuresInfo: URL | WebContent | None = None
    travelBans: URL | WebContent | None = None
    webFeed: DataFeed | URL | None = None


@dataclass
class GeospatialGeometry(Intangible):
    geoContains: GeospatialGeometry | Place | None = None
    geoCoveredBy: GeospatialGeometry | Place | None = None
    geoCovers: GeospatialGeometry | Place | None = None
    geoCrosses: GeospatialGeometry | Place | None = None
    geoDisjoint: GeospatialGeometry | Place | None = None
    geoEquals: GeospatialGeometry | Place | None = None
    geoIntersects: GeospatialGeometry | Place | None = None
    geoOverlaps: GeospatialGeometry | Place | None = None
    geoTouches: GeospatialGeometry | Place | None = None
    geoWithin: GeospatialGeometry | Place | None = None


@dataclass
class ProductGroup(Product):
    hasVariant: Product | None = None
    productGroupID: str | None = None
    variesBy: DefinedTerm | str | None = None


@dataclass
class FloorPlan(Intangible):
    amenityFeature: LocationFeatureSpecification | None = None
    floorSize: QuantitativeValue | None = None
    isPlanForApartment: Accommodation | None = None
    layoutImage: ImageObject | URL | None = None
    numberOfAccommodationUnits: QuantitativeValue | None = None
    numberOfAvailableAccommodationUnits: QuantitativeValue | None = None
    numberOfBathroomsTotal: Integer | None = None
    numberOfBedrooms: QuantitativeValue | float | None = None
    numberOfFullBathrooms: float | None = None
    numberOfPartialBathrooms: float | None = None
    numberOfRooms: QuantitativeValue | float | None = None
    petsAllowed: bool | str | None = None


@dataclass
class Movie(CreativeWork):
    actor: Person | None = None
    actors: Person | None = None
    countryOfOrigin: Country | None = None
    director: Person | None = None
    directors: Person | None = None
    duration: Duration | None = None
    musicBy: MusicGroup | Person | None = None
    productionCompany: Organization | None = None
    subtitleLanguage: Language | str | None = None
    titleEIDR: URL | str | None = None
    trailer: VideoObject | None = None


@dataclass
class HealthInsurancePlan(Intangible):
    benefitsSummaryUrl: URL | None = None
    contactPoint: ContactPoint | None = None
    healthPlanDrugOption: str | None = None
    healthPlanDrugTier: str | None = None
    healthPlanId: str | None = None
    healthPlanMarketingUrl: URL | None = None
    includesHealthPlanFormulary: HealthPlanFormulary | None = None
    includesHealthPlanNetwork: HealthPlanNetwork | None = None
    usesHealthPlanIdStandard: URL | str | None = None


@dataclass
class Trip(Intangible):
    arrivalTime: datetime.datetime | datetime.time | None = None
    departureTime: datetime.datetime | datetime.time | None = None
    itinerary: ItemList | Place | None = None
    offers: Demand | Offer | None = None
    partOfTrip: Trip | None = None
    provider: Organization | Person | None = None
    subTrip: Trip | None = None


@dataclass
class Flight(Trip):
    aircraft: Vehicle | str | None = None
    arrivalAirport: Airport | None = None
    arrivalGate: str | None = None
    arrivalTerminal: str | None = None
    boardingPolicy: BoardingPolicyType | None = None
    carrier: Organization | None = None
    departureAirport: Airport | None = None
    departureGate: str | None = None
    departureTerminal: str | None = None
    estimatedFlightDuration: Duration | str | None = None
    flightDistance: Distance | str | None = None
    flightNumber: str | None = None
    mealService: str | None = None
    seller: Organization | Person | None = None
    webCheckinTime: datetime.datetime | None = None


@dataclass
class TrainTrip(Trip):
    arrivalPlatform: str | None = None
    arrivalStation: TrainStation | None = None
    departurePlatform: str | None = None
    departureStation: TrainStation | None = None
    trainName: str | None = None
    trainNumber: str | None = None


@dataclass
class TouristTrip(Trip):
    touristType: Audience | str | None = None


@dataclass
class BoatTrip(Trip):
    arrivalBoatTerminal: BoatTerminal | None = None
    departureBoatTerminal: BoatTerminal | None = None


@dataclass
class BusTrip(Trip):
    arrivalBusStop: BusStation | BusStop | None = None
    busName: str | None = None
    busNumber: str | None = None
    departureBusStop: BusStation | BusStop | None = None


@dataclass
class Painting(CreativeWork):
    pass


@dataclass
class MedicalCondition(MedicalEntity):
    associatedAnatomy: AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy | None = None
    differentialDiagnosis: DDxElement | None = None
    drug: Drug | None = None
    epidemiology: str | None = None
    expectedPrognosis: str | None = None
    naturalProgression: str | None = None
    pathophysiology: str | None = None
    possibleComplication: str | None = None
    possibleTreatment: MedicalTherapy | None = None
    primaryPrevention: MedicalTherapy | None = None
    riskFactor: MedicalRiskFactor | None = None
    secondaryPrevention: MedicalTherapy | None = None
    signOrSymptom: MedicalSignOrSymptom | None = None
    stage: MedicalConditionStage | None = None
    status: EventStatusType | MedicalStudyStatus | str | None = None
    typicalTest: MedicalTest | None = None


@dataclass
class InfectiousDisease(MedicalCondition):
    infectiousAgent: str | None = None
    infectiousAgentClass: InfectiousAgentClass | None = None
    transmissionMethod: str | None = None


@dataclass
class MedicalSignOrSymptom(MedicalCondition):
    possibleTreatment: MedicalTherapy | None = None


@dataclass
class InteractAction(Action):
    pass


@dataclass
class MarryAction(InteractAction):
    pass


@dataclass
class SubscribeAction(InteractAction):
    pass


@dataclass
class CommunicateAction(InteractAction):
    about: Thing | None = None
    inLanguage: Language | str | None = None
    language: Language | None = None
    recipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class FollowAction(InteractAction):
    followee: Organization | Person | None = None


@dataclass
class BefriendAction(InteractAction):
    pass


@dataclass
class JoinAction(InteractAction):
    event: Event | None = None


@dataclass
class LeaveAction(InteractAction):
    event: Event | None = None


@dataclass
class UnRegisterAction(InteractAction):
    pass


@dataclass
class RegisterAction(InteractAction):
    pass


@dataclass
class ProductModel(Product):
    isVariantOf: ProductGroup | ProductModel | None = None
    predecessorOf: ProductModel | None = None
    successorOf: ProductModel | None = None


@dataclass
class MedicalStudy(MedicalEntity):
    healthCondition: MedicalCondition | None = None
    sponsor: Organization | Person | None = None
    status: EventStatusType | MedicalStudyStatus | str | None = None
    studyLocation: AdministrativeArea | None = None
    studySubject: MedicalEntity | None = None


@dataclass
class MedicalObservationalStudy(MedicalStudy):
    studyDesign: MedicalObservationalStudyDesign | None = None


@dataclass
class MedicalTrial(MedicalStudy):
    trialDesign: MedicalTrialDesign | None = None


@dataclass
class LandmarksOrHistoricalBuildings(Place):
    pass


@dataclass
class DefinedTerm(Intangible):
    inDefinedTermSet: DefinedTermSet | URL | None = None
    termCode: str | None = None


@dataclass
class CategoryCode(DefinedTerm):
    codeValue: str | None = None
    inCodeSet: CategoryCodeSet | URL | None = None


@dataclass
class HyperTocEntry(CreativeWork):
    associatedMedia: MediaObject | None = None
    tocContinuation: HyperTocEntry | None = None
    utterances: str | None = None


@dataclass
class MedicalRiskFactor(MedicalEntity):
    increasesRiskOf: MedicalEntity | None = None


@dataclass
class MedicalTest(MedicalEntity):
    affectedBy: Drug | None = None
    normalRange: MedicalEnumeration | str | None = None
    signDetected: MedicalSign | None = None
    usedToDiagnose: MedicalCondition | None = None
    usesDevice: MedicalDevice | None = None


@dataclass
class PathologyTest(MedicalTest):
    tissueSample: str | None = None


@dataclass
class MedicalTestPanel(MedicalTest):
    subTest: MedicalTest | None = None


@dataclass
class BloodTest(MedicalTest):
    pass


@dataclass
class ImagingTest(MedicalTest):
    imagingTechnique: MedicalImagingTechnique | None = None


@dataclass
class SearchRescueOrganization(Organization):
    pass


@dataclass
class ComicStory(CreativeWork):
    artist: Person | None = None
    colorist: Person | None = None
    inker: Person | None = None
    letterer: Person | None = None
    penciler: Person | None = None


@dataclass
class ComicCoverArt(ComicStory, CoverArt):
    pass


@dataclass
class HyperToc(CreativeWork):
    associatedMedia: MediaObject | None = None
    tocEntry: HyperTocEntry | None = None


@dataclass
class DigitalDocument(CreativeWork):
    hasDigitalDocumentPermission: DigitalDocumentPermission | None = None


@dataclass
class PresentationDigitalDocument(DigitalDocument):
    pass


@dataclass
class SpreadsheetDigitalDocument(DigitalDocument):
    pass


@dataclass
class TextDigitalDocument(DigitalDocument):
    pass


@dataclass
class NoteDigitalDocument(DigitalDocument):
    pass


@dataclass
class Claim(CreativeWork):
    appearance: CreativeWork | None = None
    claimInterpreter: Organization | Person | None = None
    firstAppearance: CreativeWork | None = None


@dataclass
class SaleEvent(Event):
    pass


@dataclass
class Game(CreativeWork):
    characterAttribute: Thing | None = None
    gameItem: Thing | None = None
    gameLocation: Place | PostalAddress | URL | None = None
    numberOfPlayers: QuantitativeValue | None = None
    quest: Thing | None = None


@dataclass
class VideoGame(Game, SoftwareApplication):
    actor: Person | None = None
    actors: Person | None = None
    cheatCode: CreativeWork | None = None
    director: Person | None = None
    directors: Person | None = None
    gameEdition: str | None = None
    gamePlatform: Thing | URL | str | None = None
    gameServer: GameServer | None = None
    gameTip: CreativeWork | None = None
    musicBy: MusicGroup | Person | None = None
    playMode: GamePlayMode | None = None
    trailer: VideoObject | None = None


@dataclass
class EntryPoint(Intangible):
    actionApplication: SoftwareApplication | None = None
    actionPlatform: DigitalPlatformEnumeration | URL | str | None = None
    application: SoftwareApplication | None = None
    contentType: str | None = None
    encodingType: str | None = None
    httpMethod: str | None = None
    urlTemplate: str | None = None


@dataclass
class StatisticalPopulation(Intangible):
    constrainingProperty: Integer | None = None
    numConstraints: Integer | None = None
    populationType: AbstractBase | None = None


@dataclass
class AdministrativeArea(Place):
    pass


@dataclass
class SchoolDistrict(AdministrativeArea):
    pass


@dataclass
class Country(AdministrativeArea):
    pass


@dataclass
class City(AdministrativeArea):
    pass


@dataclass
class State(AdministrativeArea):
    pass


@dataclass
class Property(Intangible):
    domainIncludes: AbstractBase | None = None
    inverseOf: Property | None = None
    rangeIncludes: AbstractBase | None = None
    supersededBy: Enumeration | Property | None = None


@dataclass
class BroadcastChannel(Intangible):
    broadcastChannelId: str | None = None
    broadcastFrequency: BroadcastFrequencySpecification | str | None = None
    broadcastServiceTier: str | None = None
    genre: URL | str | None = None
    inBroadcastLineup: CableOrSatelliteService | None = None
    providesBroadcastService: BroadcastService | None = None


@dataclass
class RadioChannel(BroadcastChannel):
    pass


@dataclass
class TelevisionChannel(BroadcastChannel):
    pass


@dataclass
class CivicStructure(Place):
    openingHours: str | None = None


@dataclass
class RVPark(CivicStructure):
    pass


@dataclass
class Airport(CivicStructure):
    iataCode: str | None = None
    icaoCode: str | None = None


@dataclass
class PerformingArtsTheater(CivicStructure):
    pass


@dataclass
class SubwayStation(CivicStructure):
    pass


@dataclass
class Bridge(CivicStructure):
    pass


@dataclass
class BoatTerminal(CivicStructure):
    pass


@dataclass
class Cemetery(CivicStructure):
    pass


@dataclass
class Museum(CivicStructure):
    pass


@dataclass
class TaxiStand(CivicStructure):
    pass


@dataclass
class Aquarium(CivicStructure):
    pass


@dataclass
class Zoo(CivicStructure):
    pass


@dataclass
class BusStop(CivicStructure):
    pass


@dataclass
class Park(CivicStructure):
    pass


@dataclass
class MusicVenue(CivicStructure):
    pass


@dataclass
class TrainStation(CivicStructure):
    pass


@dataclass
class PlaceOfWorship(CivicStructure):
    pass


@dataclass
class Playground(CivicStructure):
    pass


@dataclass
class Crematorium(CivicStructure):
    pass


@dataclass
class GovernmentBuilding(CivicStructure):
    pass


@dataclass
class EducationalOrganization(CivicStructure, Organization):
    alumni: Person | None = None


@dataclass
class ParkingFacility(CivicStructure):
    pass


@dataclass
class Beach(CivicStructure):
    pass


@dataclass
class EventVenue(CivicStructure):
    pass


@dataclass
class BusStation(CivicStructure):
    pass


@dataclass
class PublicToilet(CivicStructure):
    pass


@dataclass
class ResearchOrganization(Organization):
    pass


@dataclass
class SearchAction(Action):
    query: str | None = None


@dataclass
class BedDetails(Intangible):
    numberOfBeds: float | None = None
    typeOfBed: BedType | str | None = None


@dataclass
class ListItem(Intangible):
    item: Thing | None = None
    nextItem: ListItem | None = None
    position: Integer | str | None = None
    previousItem: ListItem | None = None


@dataclass
class HowToDirection(CreativeWork, ListItem):
    afterMedia: MediaObject | URL | None = None
    beforeMedia: MediaObject | URL | None = None
    duringMedia: MediaObject | URL | None = None
    performTime: Duration | None = None
    prepTime: Duration | None = None
    supply: HowToSupply | str | None = None
    tool: HowToTool | str | None = None
    totalTime: Duration | None = None


@dataclass
class HowToItem(ListItem):
    requiredQuantity: QuantitativeValue | float | str | None = None


@dataclass
class HowToSection(CreativeWork, ItemList, ListItem):
    steps: CreativeWork | ItemList | str | None = None


@dataclass
class HowToStep(CreativeWork, ItemList, ListItem):
    pass


@dataclass
class HowToTip(CreativeWork, ListItem):
    pass


@dataclass
class ComputerLanguage(Intangible):
    pass


@dataclass
class MenuItem(Intangible):
    menuAddOn: MenuItem | MenuSection | None = None
    nutrition: NutritionInformation | None = None
    offers: Demand | Offer | None = None
    suitableForDiet: RestrictedDiet | None = None


@dataclass
class WebSite(CreativeWork):
    issn: str | None = None


@dataclass
class Quotation(CreativeWork):
    spokenByCharacter: Organization | Person | None = None


@dataclass
class Article(CreativeWork):
    articleBody: str | None = None
    articleSection: str | None = None
    backstory: CreativeWork | str | None = None
    pageEnd: Integer | str | None = None
    pageStart: Integer | str | None = None
    pagination: str | None = None
    speakable: SpeakableSpecification | URL | None = None
    wordCount: Integer | None = None


@dataclass
class NewsArticle(Article):
    dateline: str | None = None
    printColumn: str | None = None
    printEdition: str | None = None
    printPage: str | None = None
    printSection: str | None = None


@dataclass
class SocialMediaPosting(Article):
    sharedContent: CreativeWork | None = None


@dataclass
class Report(Article):
    reportNumber: str | None = None


@dataclass
class TechArticle(Article):
    dependencies: str | None = None
    proficiencyLevel: str | None = None


@dataclass
class AdvertiserContentArticle(Article):
    pass


@dataclass
class SatiricalArticle(Article):
    pass


@dataclass
class ScholarlyArticle(Article):
    pass


@dataclass
class Chapter(CreativeWork):
    pageEnd: Integer | str | None = None
    pageStart: Integer | str | None = None
    pagination: str | None = None


@dataclass
class PublicationIssue(CreativeWork):
    issueNumber: Integer | str | None = None
    pageEnd: Integer | str | None = None
    pageStart: Integer | str | None = None
    pagination: str | None = None


@dataclass
class ComicIssue(PublicationIssue):
    artist: Person | None = None
    colorist: Person | None = None
    inker: Person | None = None
    letterer: Person | None = None
    penciler: Person | None = None
    variantCover: str | None = None


@dataclass
class PublicationVolume(CreativeWork):
    pageEnd: Integer | str | None = None
    pageStart: Integer | str | None = None
    pagination: str | None = None
    volumeNumber: Integer | str | None = None


@dataclass
class Observation(Intangible):
    marginOfError: QuantitativeValue | None = None
    measuredProperty: Property | None = None
    measuredValue: DataType | None = None
    observationDate: datetime.datetime | None = None
    observedNode: StatisticalPopulation | None = None


@dataclass
class MedicalRiskEstimator(MedicalEntity):
    estimatesRiskOf: MedicalEntity | None = None
    includedRiskFactor: MedicalRiskFactor | None = None


@dataclass
class MedicalRiskScore(MedicalRiskEstimator):
    algorithm: str | None = None


@dataclass
class MedicalRiskCalculator(MedicalRiskEstimator):
    pass


@dataclass
class ScreeningEvent(Event):
    subtitleLanguage: Language | str | None = None
    videoFormat: str | None = None
    workPresented: Movie | None = None


@dataclass
class MoveAction(Action):
    fromLocation: Place | None = None
    toLocation: Place | None = None


@dataclass
class ArriveAction(MoveAction):
    pass


@dataclass
class DepartAction(MoveAction):
    pass


@dataclass
class TravelAction(MoveAction):
    distance: Distance | None = None


@dataclass
class Manuscript(CreativeWork):
    pass


@dataclass
class MediaReviewItem(CreativeWork):
    mediaItemAppearance: MediaObject | None = None


@dataclass
class ComedyEvent(Event):
    pass


@dataclass
class Statement(CreativeWork):
    pass


@dataclass
class Seat(Intangible):
    seatNumber: str | None = None
    seatRow: str | None = None
    seatSection: str | None = None
    seatingType: QualitativeValue | str | None = None


@dataclass
class Audience(Intangible):
    audienceType: str | None = None
    geographicArea: AdministrativeArea | None = None


@dataclass
class PeopleAudience(Audience):
    healthCondition: MedicalCondition | None = None
    requiredGender: str | None = None
    requiredMaxAge: Integer | None = None
    requiredMinAge: Integer | None = None
    suggestedAge: QuantitativeValue | None = None
    suggestedGender: GenderType | str | None = None
    suggestedMaxAge: float | None = None
    suggestedMeasurement: QuantitativeValue | None = None
    suggestedMinAge: float | None = None


@dataclass
class BusinessAudience(Audience):
    numberOfEmployees: QuantitativeValue | None = None
    yearlyRevenue: QuantitativeValue | None = None
    yearsInOperation: QuantitativeValue | None = None


@dataclass
class EducationalAudience(Audience):
    educationalRole: str | None = None


@dataclass
class MedicalAudience(PeopleAudience):
    pass


@dataclass
class Researcher(Audience):
    pass


@dataclass
class Gene(BioChemEntity):
    alternativeOf: Gene | None = None
    encodesBioChemEntity: BioChemEntity | None = None
    expressedIn: AnatomicalStructure | AnatomicalSystem | BioChemEntity | DefinedTerm | None = None
    hasBioPolymerSequence: str | None = None


@dataclass
class BroadcastFrequencySpecification(Intangible):
    broadcastFrequencyValue: QuantitativeValue | float | None = None
    broadcastSignalModulation: QualitativeValue | str | None = None
    broadcastSubChannel: str | None = None


@dataclass
class SolveMathAction(Action):
    eduQuestionType: str | None = None


@dataclass
class IndividualProduct(Product):
    serialNumber: str | None = None


@dataclass
class AnatomicalSystem(MedicalEntity):
    associatedPathophysiology: str | None = None
    comprisedOf: AnatomicalStructure | AnatomicalSystem | None = None
    relatedCondition: MedicalCondition | None = None
    relatedStructure: AnatomicalStructure | None = None
    relatedTherapy: MedicalTherapy | None = None


@dataclass
class SuperficialAnatomy(MedicalEntity):
    associatedPathophysiology: str | None = None
    relatedAnatomy: AnatomicalStructure | AnatomicalSystem | None = None
    relatedCondition: MedicalCondition | None = None
    relatedTherapy: MedicalTherapy | None = None
    significance: str | None = None


@dataclass
class MedicalContraindication(MedicalEntity):
    pass


@dataclass
class TheaterEvent(Event):
    pass


@dataclass
class UpdateAction(Action):
    collection: Thing | None = None
    targetCollection: Thing | None = None


@dataclass
class DeleteAction(UpdateAction):
    pass


@dataclass
class ReplaceAction(UpdateAction):
    replacee: Thing | None = None
    replacer: Thing | None = None


@dataclass
class AddAction(UpdateAction):
    pass


@dataclass
class Enumeration(Intangible):
    supersededBy: Enumeration | Property | None = None


@dataclass
class StatusEnumeration(Enumeration):
    pass


@dataclass
class QualitativeValue(Enumeration):
    additionalProperty: PropertyValue | None = None
    equal: QualitativeValue | None = None
    greater: QualitativeValue | None = None
    greaterOrEqual: QualitativeValue | None = None
    lesser: QualitativeValue | None = None
    lesserOrEqual: QualitativeValue | None = None
    nonEqual: QualitativeValue | None = None
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | str | None = None


@dataclass
class PriceTypeEnumeration(Enumeration):
    pass


@dataclass
class BoardingPolicyType(Enumeration):
    pass


@dataclass
class OfferItemCondition(Enumeration):
    pass


@dataclass
class MeasurementTypeEnumeration(Enumeration):
    pass


@dataclass
class MusicAlbumReleaseType(Enumeration):
    pass


@dataclass
class EventAttendanceModeEnumeration(Enumeration):
    pass


@dataclass
class PaymentMethod(Enumeration):
    pass


@dataclass
class PhysicalActivityCategory(Enumeration):
    pass


@dataclass
class ItemAvailability(Enumeration):
    pass


@dataclass
class DayOfWeek(Enumeration):
    pass


@dataclass
class Specialty(Enumeration):
    pass


@dataclass
class ContactPointOption(Enumeration):
    pass


@dataclass
class HealthAspectEnumeration(Enumeration):
    pass


@dataclass
class CarUsageType(Enumeration):
    pass


@dataclass
class AdultOrientedEnumeration(Enumeration):
    pass


@dataclass
class NonprofitType(Enumeration):
    pass


@dataclass
class ReturnFeesEnumeration(Enumeration):
    pass


@dataclass
class EnergyEfficiencyEnumeration(Enumeration):
    pass


@dataclass
class LegalValueLevel(Enumeration):
    pass


@dataclass
class ReturnMethodEnumeration(Enumeration):
    pass


@dataclass
class GameAvailabilityEnumeration(Enumeration):
    pass


@dataclass
class RsvpResponseType(Enumeration):
    pass


@dataclass
class ProductReturnEnumeration(Enumeration):
    pass


@dataclass
class RefundTypeEnumeration(Enumeration):
    pass


@dataclass
class SizeGroupEnumeration(Enumeration):
    pass


@dataclass
class DeliveryMethod(Enumeration):
    pass


@dataclass
class DigitalPlatformEnumeration(Enumeration):
    pass


@dataclass
class GamePlayMode(Enumeration):
    pass


@dataclass
class DigitalDocumentPermissionType(Enumeration):
    pass


@dataclass
class GenderType(Enumeration):
    pass


@dataclass
class BusinessEntityType(Enumeration):
    pass


@dataclass
class ItemListOrderType(Enumeration):
    pass


@dataclass
class WarrantyScope(Enumeration):
    pass


@dataclass
class MapCategoryType(Enumeration):
    pass


@dataclass
class SizeSystemEnumeration(Enumeration):
    pass


@dataclass
class MusicReleaseFormatType(Enumeration):
    pass


@dataclass
class GovernmentBenefitsType(Enumeration):
    pass


@dataclass
class MediaManipulationRatingEnumeration(Enumeration):
    pass


@dataclass
class MedicalEnumeration(Enumeration):
    pass


@dataclass
class BookFormatType(Enumeration):
    pass


@dataclass
class ReturnLabelSourceEnumeration(Enumeration):
    pass


@dataclass
class BusinessFunction(Enumeration):
    pass


@dataclass
class MusicAlbumProductionType(Enumeration):
    pass


@dataclass
class RestrictedDiet(Enumeration):
    pass


@dataclass
class MerchantReturnEnumeration(Enumeration):
    pass


@dataclass
class PriceComponentTypeEnumeration(Enumeration):
    pass


@dataclass
class DefinedTermSet(CreativeWork):
    hasDefinedTerm: DefinedTerm | None = None


@dataclass
class CategoryCodeSet(DefinedTermSet):
    hasCategoryCode: CategoryCode | None = None


@dataclass
class Grant(Intangible):
    fundedItem: BioChemEntity | CreativeWork | Event | MedicalEntity | Organization | Person | Product | None = None
    funder: Organization | Person | None = None
    sponsor: Organization | Person | None = None


@dataclass
class MonetaryGrant(Grant):
    amount: MonetaryAmount | float | None = None
    funder: Organization | Person | None = None


@dataclass
class Substance(MedicalEntity):
    activeIngredient: str | None = None
    maximumIntake: MaximumDoseSchedule | None = None


@dataclass
class DietarySupplement(Substance):
    activeIngredient: str | None = None
    isProprietary: bool | None = None
    legalStatus: DrugLegalStatus | MedicalEnumeration | str | None = None
    manufacturer: Organization | None = None
    maximumIntake: MaximumDoseSchedule | None = None
    mechanismOfAction: str | None = None
    nonProprietaryName: str | None = None
    proprietaryName: str | None = None
    recommendedIntake: RecommendedDoseSchedule | None = None
    safetyConsideration: str | None = None
    targetPopulation: str | None = None


@dataclass
class Drug(Substance):
    activeIngredient: str | None = None
    administrationRoute: str | None = None
    alcoholWarning: str | None = None
    availableStrength: DrugStrength | None = None
    breastfeedingWarning: str | None = None
    clincalPharmacology: str | None = None
    clinicalPharmacology: str | None = None
    dosageForm: str | None = None
    doseSchedule: DoseSchedule | None = None
    drugClass: DrugClass | None = None
    drugUnit: str | None = None
    foodWarning: str | None = None
    includedInHealthInsurancePlan: HealthInsurancePlan | None = None
    interactingDrug: Drug | None = None
    isAvailableGenerically: bool | None = None
    isProprietary: bool | None = None
    labelDetails: URL | None = None
    legalStatus: DrugLegalStatus | MedicalEnumeration | str | None = None
    manufacturer: Organization | None = None
    maximumIntake: MaximumDoseSchedule | None = None
    mechanismOfAction: str | None = None
    nonProprietaryName: str | None = None
    overdosage: str | None = None
    pregnancyCategory: DrugPregnancyCategory | None = None
    pregnancyWarning: str | None = None
    prescribingInfo: URL | None = None
    prescriptionStatus: DrugPrescriptionStatus | str | None = None
    proprietaryName: str | None = None
    relatedDrug: Drug | None = None
    rxcui: str | None = None
    warning: URL | str | None = None


@dataclass
class WebPageElement(CreativeWork):
    cssSelector: CssSelectorType | None = None
    xpath: XPathType | None = None


@dataclass
class WPSideBar(WebPageElement):
    pass


@dataclass
class WPHeader(WebPageElement):
    pass


@dataclass
class Table(WebPageElement):
    pass


@dataclass
class SiteNavigationElement(WebPageElement):
    pass


@dataclass
class WPAdBlock(WebPageElement):
    pass


@dataclass
class WPFooter(WebPageElement):
    pass


@dataclass
class PublicationEvent(Event):
    free: bool | None = None
    publishedBy: Organization | Person | None = None
    publishedOn: BroadcastService | None = None


@dataclass
class BroadcastEvent(PublicationEvent):
    broadcastOfEvent: Event | None = None
    isLiveBroadcast: bool | None = None
    subtitleLanguage: Language | str | None = None
    videoFormat: str | None = None


@dataclass
class OnDemandEvent(PublicationEvent):
    pass


@dataclass
class Blog(CreativeWork):
    blogPost: BlogPosting | None = None
    blogPosts: BlogPosting | None = None
    issn: str | None = None


@dataclass
class Guide(CreativeWork):
    reviewAspect: str | None = None


@dataclass
class Rating(Intangible):
    author: Organization | Person | None = None
    bestRating: float | str | None = None
    ratingExplanation: str | None = None
    ratingValue: float | str | None = None
    reviewAspect: str | None = None
    worstRating: float | str | None = None


@dataclass
class EndorsementRating(Rating):
    pass


@dataclass
class AggregateRating(Rating):
    itemReviewed: Thing | None = None
    ratingCount: Integer | None = None
    reviewCount: Integer | None = None


@dataclass
class OrganizeAction(Action):
    pass


@dataclass
class PlanAction(OrganizeAction):
    scheduledTime: datetime.datetime | None = None


@dataclass
class AllocateAction(OrganizeAction):
    pass


@dataclass
class BookmarkAction(OrganizeAction):
    pass


@dataclass
class ApplyAction(OrganizeAction):
    pass


@dataclass
class MolecularEntity(BioChemEntity):
    chemicalRole: DefinedTerm | None = None
    inChI: str | None = None
    inChIKey: str | None = None
    iupacName: str | None = None
    molecularFormula: str | None = None
    molecularWeight: QuantitativeValue | str | None = None
    monoisotopicMolecularWeight: QuantitativeValue | str | None = None
    potentialUse: DefinedTerm | None = None
    smiles: str | None = None


@dataclass
class CourseInstance(Event):
    courseMode: URL | str | None = None
    courseWorkload: str | None = None
    instructor: Person | None = None


@dataclass
class Comment(CreativeWork):
    downvoteCount: Integer | None = None
    parentItem: Comment | None = None
    upvoteCount: Integer | None = None


@dataclass
class CorrectionComment(Comment):
    pass


@dataclass
class Answer(Comment):
    answerExplanation: Comment | WebContent | None = None


@dataclass
class Question(Comment):
    acceptedAnswer: Answer | ItemList | None = None
    answerCount: Integer | None = None
    eduQuestionType: str | None = None
    suggestedAnswer: Answer | ItemList | None = None


@dataclass
class Play(CreativeWork):
    pass


@dataclass
class ArchiveComponent(CreativeWork):
    holdingArchive: ArchiveOrganization | None = None
    itemLocation: Place | PostalAddress | str | None = None


@dataclass
class DataCatalog(CreativeWork):
    dataset: Dataset | None = None
    measurementTechnique: URL | str | None = None


@dataclass
class AchieveAction(Action):
    pass


@dataclass
class WinAction(AchieveAction):
    loser: Person | None = None


@dataclass
class TieAction(AchieveAction):
    pass


@dataclass
class LoseAction(AchieveAction):
    winner: Person | None = None


@dataclass
class Protein(BioChemEntity):
    hasBioPolymerSequence: str | None = None


@dataclass
class WebContent(CreativeWork):
    pass


@dataclass
class HealthTopicContent(WebContent):
    hasHealthAspect: HealthAspectEnumeration | None = None


@dataclass
class FindAction(Action):
    pass


@dataclass
class TrackAction(FindAction):
    deliveryMethod: DeliveryMethod | None = None


@dataclass
class DiscoverAction(FindAction):
    pass


@dataclass
class CheckAction(FindAction):
    pass


@dataclass
class GovernmentOrganization(Organization):
    pass


@dataclass
class DrugClass(MedicalEntity):
    drug: Drug | None = None


@dataclass
class Menu(CreativeWork):
    hasMenuItem: MenuItem | None = None
    hasMenuSection: MenuSection | None = None


@dataclass
class MenuSection(CreativeWork):
    hasMenuItem: MenuItem | None = None
    hasMenuSection: MenuSection | None = None


@dataclass
class Map(CreativeWork):
    mapType: MapCategoryType | None = None


@dataclass
class StructuredValue(Intangible):
    pass


@dataclass
class CDCPMDRecord(StructuredValue):
    cvdCollectionDate: datetime.datetime | str | None = None
    cvdFacilityCounty: str | None = None
    cvdFacilityId: str | None = None
    cvdNumBeds: float | None = None
    cvdNumBedsOcc: float | None = None
    cvdNumC19Died: float | None = None
    cvdNumC19HOPats: float | None = None
    cvdNumC19HospPats: float | None = None
    cvdNumC19MechVentPats: float | None = None
    cvdNumC19OFMechVentPats: float | None = None
    cvdNumC19OverflowPats: float | None = None
    cvdNumICUBeds: float | None = None
    cvdNumICUBedsOcc: float | None = None
    cvdNumTotBeds: float | None = None
    cvdNumVent: float | None = None
    cvdNumVentUse: float | None = None
    datePosted: datetime.date | datetime.datetime | None = None


@dataclass
class PriceSpecification(StructuredValue):
    eligibleQuantity: QuantitativeValue | None = None
    eligibleTransactionVolume: PriceSpecification | None = None
    maxPrice: float | None = None
    minPrice: float | None = None
    price: float | str | None = None
    priceCurrency: str | None = None
    validFrom: datetime.date | datetime.datetime | None = None
    validThrough: datetime.date | datetime.datetime | None = None
    valueAddedTaxIncluded: bool | None = None


@dataclass
class ShippingDeliveryTime(StructuredValue):
    businessDays: OpeningHoursSpecification | None = None
    cutoffTime: datetime.time | None = None
    handlingTime: QuantitativeValue | None = None
    transitTime: QuantitativeValue | None = None


@dataclass
class QuantitativeValueDistribution(StructuredValue):
    duration: Duration | None = None
    median: float | None = None
    percentile10: float | None = None
    percentile25: float | None = None
    percentile75: float | None = None
    percentile90: float | None = None


@dataclass
class DeliveryTimeSettings(StructuredValue):
    deliveryTime: ShippingDeliveryTime | None = None
    isUnlabelledFallback: bool | None = None
    shippingDestination: DefinedRegion | None = None
    transitTimeLabel: str | None = None


@dataclass
class OfferShippingDetails(StructuredValue):
    deliveryTime: ShippingDeliveryTime | None = None
    doesNotShip: bool | None = None
    shippingDestination: DefinedRegion | None = None
    shippingLabel: str | None = None
    shippingRate: MonetaryAmount | None = None
    shippingSettingsLink: URL | None = None
    transitTimeLabel: str | None = None


@dataclass
class ShippingRateSettings(StructuredValue):
    doesNotShip: bool | None = None
    freeShippingThreshold: DeliveryChargeSpecification | MonetaryAmount | None = None
    isUnlabelledFallback: bool | None = None
    shippingDestination: DefinedRegion | None = None
    shippingLabel: str | None = None
    shippingRate: MonetaryAmount | None = None


@dataclass
class ContactPoint(StructuredValue):
    areaServed: AdministrativeArea | GeoShape | Place | str | None = None
    availableLanguage: Language | str | None = None
    contactOption: ContactPointOption | None = None
    contactType: str | None = None
    email: str | None = None
    faxNumber: str | None = None
    hoursAvailable: OpeningHoursSpecification | None = None
    productSupported: Product | str | None = None
    serviceArea: AdministrativeArea | GeoShape | Place | None = None
    telephone: str | None = None


@dataclass
class PropertyValue(StructuredValue):
    maxValue: float | None = None
    measurementTechnique: URL | str | None = None
    minValue: float | None = None
    propertyID: URL | str | None = None
    unitCode: URL | str | None = None
    unitText: str | None = None
    value: StructuredValue | bool | float | str | None = None
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | str | None = None


@dataclass
class QuantitativeValue(StructuredValue):
    additionalProperty: PropertyValue | None = None
    maxValue: float | None = None
    minValue: float | None = None
    unitCode: URL | str | None = None
    unitText: str | None = None
    value: StructuredValue | bool | float | str | None = None
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | str | None = None


@dataclass
class DefinedRegion(StructuredValue):
    addressCountry: Country | str | None = None
    addressRegion: str | None = None
    postalCode: str | None = None
    postalCodePrefix: str | None = None
    postalCodeRange: PostalCodeRangeSpecification | None = None


@dataclass
class GeoCoordinates(StructuredValue):
    address: PostalAddress | str | None = None
    addressCountry: Country | str | None = None
    elevation: float | str | None = None
    latitude: float | str | None = None
    longitude: float | str | None = None
    postalCode: str | None = None


@dataclass
class GeoShape(StructuredValue):
    address: PostalAddress | str | None = None
    addressCountry: Country | str | None = None
    box: str | None = None
    circle: str | None = None
    elevation: float | str | None = None
    line: str | None = None
    polygon: str | None = None
    postalCode: str | None = None


@dataclass
class NutritionInformation(StructuredValue):
    calories: Energy | None = None
    carbohydrateContent: Mass | None = None
    cholesterolContent: Mass | None = None
    fatContent: Mass | None = None
    fiberContent: Mass | None = None
    proteinContent: Mass | None = None
    saturatedFatContent: Mass | None = None
    servingSize: str | None = None
    sodiumContent: Mass | None = None
    sugarContent: Mass | None = None
    transFatContent: Mass | None = None
    unsaturatedFatContent: Mass | None = None


@dataclass
class OwnershipInfo(StructuredValue):
    acquiredFrom: Organization | Person | None = None
    ownedFrom: datetime.datetime | None = None
    ownedThrough: datetime.datetime | None = None
    typeOfGood: Product | Service | None = None


@dataclass
class DatedMoneySpecification(StructuredValue):
    amount: MonetaryAmount | float | None = None
    currency: str | None = None
    endDate: datetime.date | datetime.datetime | None = None
    startDate: datetime.date | datetime.datetime | None = None


@dataclass
class OpeningHoursSpecification(StructuredValue):
    closes: datetime.time | None = None
    dayOfWeek: DayOfWeek | None = None
    opens: datetime.time | None = None
    validFrom: datetime.date | datetime.datetime | None = None
    validThrough: datetime.date | datetime.datetime | None = None


@dataclass
class RepaymentSpecification(StructuredValue):
    downPayment: MonetaryAmount | float | None = None
    earlyPrepaymentPenalty: MonetaryAmount | None = None
    loanPaymentAmount: MonetaryAmount | None = None
    loanPaymentFrequency: float | None = None
    numberOfLoanPayments: float | None = None


@dataclass
class MonetaryAmount(StructuredValue):
    currency: str | None = None
    maxValue: float | None = None
    minValue: float | None = None
    validFrom: datetime.date | datetime.datetime | None = None
    validThrough: datetime.date | datetime.datetime | None = None
    value: StructuredValue | bool | float | str | None = None


@dataclass
class TypeAndQuantityNode(StructuredValue):
    amountOfThisGood: float | None = None
    businessFunction: BusinessFunction | None = None
    typeOfGood: Product | Service | None = None
    unitCode: URL | str | None = None
    unitText: str | None = None


@dataclass
class InteractionCounter(StructuredValue):
    endTime: datetime.datetime | datetime.time | None = None
    interactionService: SoftwareApplication | WebSite | None = None
    interactionType: Action | None = None
    location: Place | PostalAddress | VirtualLocation | str | None = None
    startTime: datetime.datetime | datetime.time | None = None
    userInteractionCount: Integer | None = None


@dataclass
class EngineSpecification(StructuredValue):
    engineDisplacement: QuantitativeValue | None = None
    enginePower: QuantitativeValue | None = None
    engineType: QualitativeValue | URL | str | None = None
    fuelType: QualitativeValue | URL | str | None = None
    torque: QuantitativeValue | None = None


@dataclass
class ExchangeRateSpecification(StructuredValue):
    currency: str | None = None
    currentExchangeRate: UnitPriceSpecification | None = None
    exchangeRateSpread: MonetaryAmount | float | None = None


@dataclass
class PostalCodeRangeSpecification(StructuredValue):
    postalCodeBegin: str | None = None
    postalCodeEnd: str | None = None


@dataclass
class WarrantyPromise(StructuredValue):
    durationOfWarranty: QuantitativeValue | None = None
    warrantyScope: WarrantyScope | None = None


@dataclass
class TransferAction(Action):
    fromLocation: Place | None = None
    toLocation: Place | None = None


@dataclass
class MoneyTransfer(TransferAction):
    amount: MonetaryAmount | float | None = None
    beneficiaryBank: BankOrCreditUnion | str | None = None


@dataclass
class GiveAction(TransferAction):
    recipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class ReturnAction(TransferAction):
    recipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class SendAction(TransferAction):
    deliveryMethod: DeliveryMethod | None = None
    recipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class LendAction(TransferAction):
    borrower: Person | None = None


@dataclass
class ReceiveAction(TransferAction):
    deliveryMethod: DeliveryMethod | None = None
    sender: Audience | Organization | Person | None = None


@dataclass
class BorrowAction(TransferAction):
    lender: Organization | Person | None = None


@dataclass
class DownloadAction(TransferAction):
    pass


@dataclass
class TakeAction(TransferAction):
    pass


@dataclass
class Photograph(CreativeWork):
    pass


@dataclass
class Residence(Place):
    accommodationFloorPlan: FloorPlan | None = None


@dataclass
class GatedResidenceCommunity(Residence):
    pass


@dataclass
class ApartmentComplex(Residence):
    numberOfAccommodationUnits: QuantitativeValue | None = None
    numberOfAvailableAccommodationUnits: QuantitativeValue | None = None
    numberOfBedrooms: QuantitativeValue | float | None = None
    petsAllowed: bool | str | None = None
    tourBookingPage: URL | None = None


@dataclass
class Conversation(CreativeWork):
    pass


@dataclass
class LifestyleModification(MedicalEntity):
    pass


@dataclass
class Diet(CreativeWork, LifestyleModification):
    dietFeatures: str | None = None
    endorsers: Organization | Person | None = None
    expertConsiderations: str | None = None
    physiologicalBenefits: str | None = None
    risks: str | None = None


@dataclass
class PhysicalActivity(LifestyleModification):
    associatedAnatomy: AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy | None = None
    category: CategoryCode | PhysicalActivityCategory | Thing | URL | str | None = None
    epidemiology: str | None = None
    pathophysiology: str | None = None


@dataclass
class Atlas(CreativeWork):
    pass


@dataclass
class Season(CreativeWork):
    pass


@dataclass
class SportsOrganization(Organization):
    sport: URL | str | None = None


@dataclass
class SportsTeam(SportsOrganization):
    athlete: Person | None = None
    coach: Person | None = None
    gender: GenderType | str | None = None


@dataclass
class Thesis(CreativeWork):
    inSupportOf: str | None = None


@dataclass
class SomeProducts(Product):
    inventoryLevel: QuantitativeValue | None = None


@dataclass
class Code(CreativeWork):
    pass


@dataclass
class BusinessEvent(Event):
    pass


@dataclass
class AssessAction(Action):
    pass


@dataclass
class IgnoreAction(AssessAction):
    pass


@dataclass
class ChooseAction(AssessAction):
    actionOption: Thing | str | None = None
    option: Thing | str | None = None


@dataclass
class ReviewAction(AssessAction):
    resultReview: Review | None = None


@dataclass
class ReactAction(AssessAction):
    pass


@dataclass
class Series(Intangible):
    pass


@dataclass
class CreativeWorkSeries(CreativeWork, Series):
    endDate: datetime.date | datetime.datetime | None = None
    issn: str | None = None
    startDate: datetime.date | datetime.datetime | None = None


@dataclass
class EventSeries(Event, Series):
    pass


@dataclass
class Language(Intangible):
    pass


@dataclass
class MusicEvent(Event):
    pass


@dataclass
class TradeAction(Action):
    price: float | str | None = None
    priceCurrency: str | None = None
    priceSpecification: PriceSpecification | None = None


@dataclass
class BuyAction(TradeAction):
    seller: Organization | Person | None = None
    vendor: Organization | Person | None = None
    warrantyPromise: WarrantyPromise | None = None


@dataclass
class SellAction(TradeAction):
    buyer: Organization | Person | None = None
    warrantyPromise: WarrantyPromise | None = None


@dataclass
class TipAction(TradeAction):
    recipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class DonateAction(TradeAction):
    recipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class PayAction(TradeAction):
    recipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class OrderAction(TradeAction):
    deliveryMethod: DeliveryMethod | None = None


@dataclass
class QuoteAction(TradeAction):
    pass


@dataclass
class RentAction(TradeAction):
    landlord: Organization | Person | None = None
    realEstateAgent: RealEstateAgent | None = None


@dataclass
class PreOrderAction(TradeAction):
    pass


@dataclass
class OccupationalExperienceRequirements(Intangible):
    monthsOfExperience: float | None = None


@dataclass
class ChemicalSubstance(BioChemEntity):
    chemicalComposition: str | None = None
    chemicalRole: DefinedTerm | None = None
    potentialUse: DefinedTerm | None = None


@dataclass
class Collection(CreativeWork):
    collectionSize: Integer | None = None


@dataclass
class ProductCollection(Collection, Product):
    includesObject: TypeAndQuantityNode | None = None


@dataclass
class LibrarySystem(Organization):
    pass


@dataclass
class Project(Organization):
    pass


@dataclass
class FundingAgency(Project):
    pass


@dataclass
class ResearchProject(Project):
    pass


@dataclass
class DigitalDocumentPermission(Intangible):
    grantee: Audience | ContactPoint | Organization | Person | None = None
    permissionType: DigitalDocumentPermissionType | None = None


@dataclass
class WorkersUnion(Organization):
    pass


@dataclass
class ChildrensEvent(Event):
    pass


@dataclass
class OnlineBusiness(Organization):
    pass


@dataclass
class OnlineStore(OnlineBusiness):
    pass


@dataclass
class Class(Intangible):
    pass


@dataclass
class VisualArtsEvent(Event):
    pass


@dataclass
class Consortium(Organization):
    pass


@dataclass
class FoodEvent(Event):
    pass


@dataclass
class LiteraryEvent(Event):
    pass


@dataclass
class ControlAction(Action):
    pass


@dataclass
class SuspendAction(ControlAction):
    pass


@dataclass
class DeactivateAction(ControlAction):
    pass


@dataclass
class ResumeAction(ControlAction):
    pass


@dataclass
class ActivateAction(ControlAction):
    pass


@dataclass
class SheetMusic(CreativeWork):
    pass


@dataclass
class ExhibitionEvent(Event):
    pass


@dataclass
class PerformingGroup(Organization):
    pass


@dataclass
class MusicGroup(PerformingGroup):
    album: MusicAlbum | None = None
    albums: MusicAlbum | None = None
    genre: URL | str | None = None
    musicGroupMember: Person | None = None
    track: ItemList | MusicRecording | None = None
    tracks: MusicRecording | None = None


@dataclass
class DanceGroup(PerformingGroup):
    pass


@dataclass
class TheaterGroup(PerformingGroup):
    pass


@dataclass
class VirtualLocation(Intangible):
    pass


@dataclass
class Hackathon(Event):
    pass


@dataclass
class CreateAction(Action):
    pass


@dataclass
class PaintAction(CreateAction):
    pass


@dataclass
class CookAction(CreateAction):
    foodEstablishment: FoodEstablishment | Place | None = None
    foodEvent: FoodEvent | None = None
    recipe: Recipe | None = None


@dataclass
class PhotographAction(CreateAction):
    pass


@dataclass
class WriteAction(CreateAction):
    inLanguage: Language | str | None = None
    language: Language | None = None


@dataclass
class DrawAction(CreateAction):
    pass


@dataclass
class FilmAction(CreateAction):
    pass


@dataclass
class MedicalIntangible(MedicalEntity):
    pass


@dataclass
class DoseSchedule(MedicalIntangible):
    doseUnit: str | None = None
    doseValue: QualitativeValue | float | None = None
    frequency: str | None = None
    targetPopulation: str | None = None


@dataclass
class DrugStrength(MedicalIntangible):
    activeIngredient: str | None = None
    availableIn: AdministrativeArea | None = None
    maximumIntake: MaximumDoseSchedule | None = None
    strengthUnit: str | None = None
    strengthValue: float | None = None


@dataclass
class DrugLegalStatus(MedicalIntangible):
    applicableLocation: AdministrativeArea | None = None


@dataclass
class MedicalCode(CategoryCode, MedicalIntangible):
    codeValue: str | None = None
    codingSystem: str | None = None


@dataclass
class MedicalConditionStage(MedicalIntangible):
    stageAsNumber: float | None = None
    subStageSuffix: str | None = None


@dataclass
class DDxElement(MedicalIntangible):
    diagnosis: MedicalCondition | None = None
    distinguishingSign: MedicalSignOrSymptom | None = None


@dataclass
class MedicalIndication(MedicalEntity):
    pass


@dataclass
class ApprovedIndication(MedicalIndication):
    pass


@dataclass
class PreventionIndication(MedicalIndication):
    pass


@dataclass
class TreatmentIndication(MedicalIndication):
    pass


@dataclass
class Landform(Place):
    pass


@dataclass
class Mountain(Landform):
    pass


@dataclass
class Continent(Landform):
    pass


@dataclass
class BodyOfWater(Landform):
    pass


@dataclass
class Volcano(Landform):
    pass


@dataclass
class Poster(CreativeWork):
    pass


@dataclass
class UserInteraction(Event):
    pass


@dataclass
class UserPageVisits(UserInteraction):
    pass


@dataclass
class UserLikes(UserInteraction):
    pass


@dataclass
class UserPlusOnes(UserInteraction):
    pass


@dataclass
class UserComments(UserInteraction):
    commentText: str | None = None
    commentTime: datetime.date | datetime.datetime | None = None
    creator: Organization | Person | None = None
    discusses: CreativeWork | None = None
    replyToUrl: URL | None = None


@dataclass
class UserTweets(UserInteraction):
    pass


@dataclass
class UserCheckins(UserInteraction):
    pass


@dataclass
class UserDownloads(UserInteraction):
    pass


@dataclass
class UserPlays(UserInteraction):
    pass


@dataclass
class UserBlocks(UserInteraction):
    pass


@dataclass
class Quantity(Intangible):
    pass


@dataclass
class Energy(Quantity):
    pass


@dataclass
class Duration(Quantity):
    pass


@dataclass
class Mass(Quantity):
    pass


@dataclass
class Distance(Quantity):
    pass


@dataclass
class Sculpture(CreativeWork):
    pass


@dataclass
class LocalBusiness(Organization, Place):
    branchOf: Organization | None = None
    currenciesAccepted: str | None = None
    openingHours: str | None = None
    paymentAccepted: str | None = None
    priceRange: str | None = None


@dataclass
class InternetCafe(LocalBusiness):
    pass


@dataclass
class TelevisionStation(LocalBusiness):
    pass


@dataclass
class TravelAgency(LocalBusiness):
    pass


@dataclass
class FoodEstablishment(LocalBusiness):
    acceptsReservations: URL | bool | str | None = None
    hasMenu: Menu | URL | str | None = None
    menu: Menu | URL | str | None = None
    servesCuisine: str | None = None
    starRating: Rating | None = None


@dataclass
class RadioStation(LocalBusiness):
    pass


@dataclass
class SportsActivityLocation(LocalBusiness):
    pass


@dataclass
class ChildCare(LocalBusiness):
    pass


@dataclass
class GovernmentOffice(LocalBusiness):
    pass


@dataclass
class HealthAndBeautyBusiness(LocalBusiness):
    pass


@dataclass
class LodgingBusiness(LocalBusiness):
    amenityFeature: LocationFeatureSpecification | None = None
    audience: Audience | None = None
    availableLanguage: Language | str | None = None
    checkinTime: datetime.datetime | datetime.time | None = None
    checkoutTime: datetime.datetime | datetime.time | None = None
    numberOfRooms: QuantitativeValue | float | None = None
    petsAllowed: bool | str | None = None
    starRating: Rating | None = None


@dataclass
class AutomotiveBusiness(LocalBusiness):
    pass


@dataclass
class FinancialService(LocalBusiness):
    feesAndCommissionsSpecification: URL | str | None = None


@dataclass
class RecyclingCenter(LocalBusiness):
    pass


@dataclass
class Store(LocalBusiness):
    pass


@dataclass
class LegalService(LocalBusiness):
    pass


@dataclass
class ArchiveOrganization(LocalBusiness):
    archiveHeld: ArchiveComponent | None = None


@dataclass
class SelfStorage(LocalBusiness):
    pass


@dataclass
class ShoppingCenter(LocalBusiness):
    pass


@dataclass
class EntertainmentBusiness(LocalBusiness):
    pass


@dataclass
class EmergencyService(LocalBusiness):
    pass


@dataclass
class EmploymentAgency(LocalBusiness):
    pass


@dataclass
class ProfessionalService(LocalBusiness):
    pass


@dataclass
class HomeAndConstructionBusiness(LocalBusiness):
    pass


@dataclass
class RealEstateAgent(LocalBusiness):
    pass


@dataclass
class MedicalBusiness(LocalBusiness):
    pass


@dataclass
class AnimalShelter(LocalBusiness):
    pass


@dataclass
class Library(LocalBusiness):
    pass


@dataclass
class DryCleaningOrLaundry(LocalBusiness):
    pass


@dataclass
class TouristInformationCenter(LocalBusiness):
    pass


@dataclass
class HotelRoom(Room):
    bed: BedDetails | BedType | str | None = None
    occupancy: QuantitativeValue | None = None


@dataclass
class SingleFamilyResidence(House):
    numberOfRooms: QuantitativeValue | float | None = None
    occupancy: QuantitativeValue | None = None


@dataclass
class MeetingRoom(Room):
    pass


@dataclass
class CompleteDataFeed(DataFeed):
    pass


@dataclass
class VideoObjectSnapshot(VideoObject):
    pass


@dataclass
class ImageObjectSnapshot(ImageObject):
    pass


@dataclass
class AudioObjectSnapshot(AudioObject):
    pass


@dataclass
class Barcode(ImageObject):
    pass


@dataclass
class Audiobook(AudioObject, Book):
    duration: Duration | None = None
    readBy: Person | None = None


@dataclass
class MedicalTherapy(TherapeuticProcedure):
    contraindication: MedicalContraindication | str | None = None
    duplicateTherapy: MedicalTherapy | None = None
    seriousAdverseOutcome: MedicalEntity | None = None


@dataclass
class RadiationTherapy(MedicalTherapy):
    pass


@dataclass
class PalliativeProcedure(MedicalTherapy):
    pass


@dataclass
class PhysicalTherapy(MedicalTherapy):
    pass


@dataclass
class OccupationalTherapy(MedicalTherapy):
    pass


@dataclass
class PsychologicalTreatment(TherapeuticProcedure):
    pass


@dataclass
class MediaGallery(CollectionPage):
    pass


@dataclass
class VideoGallery(MediaGallery):
    pass


@dataclass
class ImageGallery(MediaGallery):
    pass


@dataclass
class WearAction(UseAction):
    pass


@dataclass
class Artery(Vessel):
    arterialBranch: AnatomicalStructure | None = None
    supplyTo: AnatomicalStructure | None = None


@dataclass
class LymphaticVessel(Vessel):
    originatesFrom: Vessel | None = None
    regionDrained: AnatomicalStructure | AnatomicalSystem | None = None
    runsTo: Vessel | None = None


@dataclass
class Vein(Vessel):
    drainsTo: Vessel | None = None
    regionDrained: AnatomicalStructure | AnatomicalSystem | None = None
    tributary: AnatomicalStructure | None = None


@dataclass
class EmployeeRole(OrganizationRole):
    baseSalary: MonetaryAmount | PriceSpecification | float | None = None
    salaryCurrency: str | None = None


@dataclass
class InvestmentOrDeposit(FinancialProduct):
    amount: MonetaryAmount | float | None = None


@dataclass
class BrokerageAccount(InvestmentOrDeposit):
    pass


@dataclass
class InvestmentFund(InvestmentOrDeposit):
    pass


@dataclass
class CurrencyConversionService(FinancialProduct):
    pass


@dataclass
class BankAccount(FinancialProduct):
    accountMinimumInflow: MonetaryAmount | None = None
    accountOverdraftLimit: MonetaryAmount | None = None
    bankAccountType: URL | str | None = None


@dataclass
class DepositAccount(BankAccount, InvestmentOrDeposit):
    pass


@dataclass
class LoanOrCredit(FinancialProduct):
    amount: MonetaryAmount | float | None = None
    currency: str | None = None
    gracePeriod: Duration | None = None
    loanRepaymentForm: RepaymentSpecification | None = None
    loanTerm: QuantitativeValue | None = None
    loanType: URL | str | None = None
    recourseLoan: bool | None = None
    renegotiableLoan: bool | None = None
    requiredCollateral: Thing | str | None = None


@dataclass
class MortgageLoan(LoanOrCredit):
    domiciledMortgage: bool | None = None
    loanMortgageMandateAmount: MonetaryAmount | None = None


@dataclass
class RadioBroadcastService(BroadcastService):
    pass


@dataclass
class PaymentService(FinancialProduct):
    pass


@dataclass
class MedicalSign(MedicalSignOrSymptom):
    identifyingExam: PhysicalExam | None = None
    identifyingTest: MedicalTest | None = None


@dataclass
class VitalSign(MedicalSign):
    pass


@dataclass
class MedicalSymptom(MedicalSignOrSymptom):
    pass


@dataclass
class CheckOutAction(CommunicateAction):
    pass


@dataclass
class AskAction(CommunicateAction):
    question: Question | None = None


@dataclass
class InformAction(CommunicateAction):
    event: Event | None = None


@dataclass
class RsvpAction(InformAction):
    additionalNumberOfGuests: float | None = None
    comment: Comment | None = None
    rsvpResponse: RsvpResponseType | None = None


@dataclass
class ConfirmAction(InformAction):
    pass


@dataclass
class ReplyAction(CommunicateAction):
    resultComment: Comment | None = None


@dataclass
class CheckInAction(CommunicateAction):
    pass


@dataclass
class ShareAction(CommunicateAction):
    pass


@dataclass
class InviteAction(CommunicateAction):
    event: Event | None = None


@dataclass
class CommentAction(CommunicateAction):
    resultComment: Comment | None = None


@dataclass
class AMRadioChannel(RadioChannel):
    pass


@dataclass
class FMRadioChannel(RadioChannel):
    pass


@dataclass
class ElementarySchool(EducationalOrganization):
    pass


@dataclass
class LegislativeBuilding(GovernmentBuilding):
    pass


@dataclass
class Mosque(PlaceOfWorship):
    pass


@dataclass
class Courthouse(GovernmentBuilding):
    pass


@dataclass
class School(EducationalOrganization):
    pass


@dataclass
class Synagogue(PlaceOfWorship):
    pass


@dataclass
class BuddhistTemple(PlaceOfWorship):
    pass


@dataclass
class HinduTemple(PlaceOfWorship):
    pass


@dataclass
class HighSchool(EducationalOrganization):
    pass


@dataclass
class MiddleSchool(EducationalOrganization):
    pass


@dataclass
class Preschool(EducationalOrganization):
    pass


@dataclass
class CollegeOrUniversity(EducationalOrganization):
    pass


@dataclass
class CityHall(GovernmentBuilding):
    pass


@dataclass
class Church(PlaceOfWorship):
    pass


@dataclass
class CatholicChurch(Church):
    pass


@dataclass
class Embassy(GovernmentBuilding):
    pass


@dataclass
class DefenceEstablishment(GovernmentBuilding):
    pass


@dataclass
class HowToSupply(HowToItem):
    estimatedCost: MonetaryAmount | str | None = None


@dataclass
class HowToTool(HowToItem):
    pass


@dataclass
class MedicalScholarlyArticle(ScholarlyArticle):
    publicationType: str | None = None


@dataclass
class APIReference(TechArticle):
    assembly: str | None = None
    assemblyVersion: str | None = None
    executableLibraryName: str | None = None
    programmingModel: str | None = None
    targetPlatform: str | None = None


@dataclass
class OpinionNewsArticle(NewsArticle):
    pass


@dataclass
class DiscussionForumPosting(SocialMediaPosting):
    pass


@dataclass
class BackgroundNewsArticle(NewsArticle):
    pass


@dataclass
class AnalysisNewsArticle(NewsArticle):
    pass


@dataclass
class BlogPosting(SocialMediaPosting):
    pass


@dataclass
class LiveBlogPosting(BlogPosting):
    coverageEndTime: datetime.datetime | None = None
    coverageStartTime: datetime.datetime | None = None
    liveBlogUpdate: BlogPosting | None = None


@dataclass
class AskPublicNewsArticle(NewsArticle):
    pass


@dataclass
class ReportageNewsArticle(NewsArticle):
    pass


@dataclass
class ReviewNewsArticle(CriticReview, NewsArticle):
    pass


@dataclass
class ParentAudience(PeopleAudience):
    childMaxAge: float | None = None
    childMinAge: float | None = None


@dataclass
class Patient(MedicalAudience, Person):
    diagnosis: MedicalCondition | None = None
    drug: Drug | None = None
    healthCondition: MedicalCondition | None = None


@dataclass
class InsertAction(AddAction):
    toLocation: Place | None = None


@dataclass
class AppendAction(InsertAction):
    pass


@dataclass
class PrependAction(InsertAction):
    pass


@dataclass
class NLNonprofitType(NonprofitType):
    pass


@dataclass
class WearableSizeGroupEnumeration(SizeGroupEnumeration):
    pass


@dataclass
class DrugCostCategory(MedicalEnumeration):
    pass


@dataclass
class MedicalProcedureType(MedicalEnumeration):
    pass


@dataclass
class PaymentStatusType(StatusEnumeration):
    pass


@dataclass
class BodyMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    pass


@dataclass
class InfectiousAgentClass(MedicalEnumeration):
    pass


@dataclass
class MedicalEvidenceLevel(MedicalEnumeration):
    pass


@dataclass
class SizeSpecification(QualitativeValue):
    hasMeasurement: QuantitativeValue | None = None
    sizeGroup: SizeGroupEnumeration | str | None = None
    sizeSystem: SizeSystemEnumeration | str | None = None
    suggestedAge: QuantitativeValue | None = None
    suggestedGender: GenderType | str | None = None
    suggestedMeasurement: QuantitativeValue | None = None


@dataclass
class LegalForceStatus(StatusEnumeration):
    pass


@dataclass
class MedicalImagingTechnique(MedicalEnumeration):
    pass


@dataclass
class MedicineSystem(MedicalEnumeration):
    pass


@dataclass
class MedicalObservationalStudyDesign(MedicalEnumeration):
    pass


@dataclass
class DrugPregnancyCategory(MedicalEnumeration):
    pass


@dataclass
class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    pass


@dataclass
class UKNonprofitType(NonprofitType):
    pass


@dataclass
class SteeringPositionValue(QualitativeValue):
    pass


@dataclass
class EnergyStarEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    pass


@dataclass
class GameServerStatus(StatusEnumeration):
    pass


@dataclass
class MedicalStudyStatus(MedicalEnumeration):
    pass


@dataclass
class MedicalAudienceType(MedicalEnumeration):
    pass


@dataclass
class OrderStatus(StatusEnumeration):
    pass


@dataclass
class USNonprofitType(NonprofitType):
    pass


@dataclass
class DriveWheelConfigurationValue(QualitativeValue):
    pass


@dataclass
class BedType(QualitativeValue):
    pass


@dataclass
class EventStatusType(StatusEnumeration):
    pass


@dataclass
class WearableMeasurementTypeEnumeration(MeasurementTypeEnumeration):
    pass


@dataclass
class ReservationStatusType(StatusEnumeration):
    pass


@dataclass
class DrugPrescriptionStatus(MedicalEnumeration):
    pass


@dataclass
class MedicalTrialDesign(MedicalEnumeration):
    pass


@dataclass
class WearableSizeSystemEnumeration(SizeSystemEnumeration):
    pass


@dataclass
class MedicalDevicePurpose(MedicalEnumeration):
    pass


@dataclass
class ActionStatusType(StatusEnumeration):
    pass


@dataclass
class PhysicalExam(MedicalEnumeration, MedicalProcedure):
    pass


@dataclass
class PaymentCard(FinancialProduct, PaymentMethod):
    cashBack: bool | float | None = None
    contactlessPayment: bool | None = None
    floorLimit: MonetaryAmount | None = None
    monthlyMinimumRepaymentAmount: MonetaryAmount | float | None = None


@dataclass
class CreditCard(LoanOrCredit, PaymentCard):
    pass


@dataclass
class MedicalSpecialty(MedicalEnumeration, Specialty):
    pass


@dataclass
class EmployerAggregateRating(AggregateRating):
    pass


@dataclass
class AuthorizeAction(AllocateAction):
    recipient: Audience | ContactPoint | Organization | Person | None = None


@dataclass
class CancelAction(PlanAction):
    pass


@dataclass
class AcceptAction(AllocateAction):
    pass


@dataclass
class AssignAction(AllocateAction):
    pass


@dataclass
class RejectAction(AllocateAction):
    pass


@dataclass
class ReserveAction(PlanAction):
    pass


@dataclass
class ScheduleAction(PlanAction):
    pass


@dataclass
class PostalAddress(ContactPoint):
    addressCountry: Country | str | None = None
    addressLocality: str | None = None
    addressRegion: str | None = None
    postOfficeBoxNumber: str | None = None
    postalCode: str | None = None
    streetAddress: str | None = None


@dataclass
class CompoundPriceSpecification(PriceSpecification):
    priceComponent: UnitPriceSpecification | None = None
    priceType: PriceTypeEnumeration | str | None = None


@dataclass
class GeoCircle(GeoShape):
    geoMidpoint: GeoCoordinates | None = None
    geoRadius: Distance | float | str | None = None


@dataclass
class UnitPriceSpecification(PriceSpecification):
    billingDuration: Duration | QuantitativeValue | float | None = None
    billingIncrement: float | None = None
    billingStart: float | None = None
    priceComponentType: PriceComponentTypeEnumeration | None = None
    priceType: PriceTypeEnumeration | str | None = None
    referenceQuantity: QuantitativeValue | None = None
    unitCode: URL | str | None = None
    unitText: str | None = None


@dataclass
class LocationFeatureSpecification(PropertyValue):
    hoursAvailable: OpeningHoursSpecification | None = None
    validFrom: datetime.date | datetime.datetime | None = None
    validThrough: datetime.date | datetime.datetime | None = None


@dataclass
class DeliveryChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: DeliveryMethod | None = None
    areaServed: AdministrativeArea | GeoShape | Place | str | None = None
    eligibleRegion: GeoShape | Place | str | None = None
    ineligibleRegion: GeoShape | Place | str | None = None


@dataclass
class PaymentChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: DeliveryMethod | None = None
    appliesToPaymentMethod: PaymentMethod | None = None


@dataclass
class MonetaryAmountDistribution(QuantitativeValueDistribution):
    currency: str | None = None


@dataclass
class ExercisePlan(CreativeWork, PhysicalActivity):
    activityDuration: Duration | QuantitativeValue | None = None
    activityFrequency: QuantitativeValue | str | None = None
    additionalVariable: str | None = None
    exerciseType: str | None = None
    intensity: QuantitativeValue | str | None = None
    repetitions: QuantitativeValue | float | None = None
    restPeriods: QuantitativeValue | str | None = None
    workload: Energy | QuantitativeValue | None = None


@dataclass
class VoteAction(ChooseAction):
    candidate: Person | None = None


@dataclass
class DisagreeAction(ReactAction):
    pass


@dataclass
class LikeAction(ReactAction):
    pass


@dataclass
class EndorseAction(ReactAction):
    endorsee: Organization | Person | None = None


@dataclass
class AgreeAction(ReactAction):
    pass


@dataclass
class WantAction(ReactAction):
    pass


@dataclass
class DislikeAction(ReactAction):
    pass


@dataclass
class RadioSeries(CreativeWorkSeries):
    actor: Person | None = None
    actors: Person | None = None
    containsSeason: CreativeWorkSeason | None = None
    director: Person | None = None
    directors: Person | None = None
    episode: Episode | None = None
    episodes: Episode | None = None
    musicBy: MusicGroup | Person | None = None
    numberOfEpisodes: Integer | None = None
    numberOfSeasons: Integer | None = None
    productionCompany: Organization | None = None
    season: CreativeWorkSeason | URL | None = None
    seasons: CreativeWorkSeason | None = None
    trailer: VideoObject | None = None


@dataclass
class VideoGameSeries(CreativeWorkSeries):
    actor: Person | None = None
    actors: Person | None = None
    characterAttribute: Thing | None = None
    cheatCode: CreativeWork | None = None
    containsSeason: CreativeWorkSeason | None = None
    director: Person | None = None
    directors: Person | None = None
    episode: Episode | None = None
    episodes: Episode | None = None
    gameItem: Thing | None = None
    gameLocation: Place | PostalAddress | URL | None = None
    gamePlatform: Thing | URL | str | None = None
    musicBy: MusicGroup | Person | None = None
    numberOfEpisodes: Integer | None = None
    numberOfPlayers: QuantitativeValue | None = None
    numberOfSeasons: Integer | None = None
    playMode: GamePlayMode | None = None
    productionCompany: Organization | None = None
    quest: Thing | None = None
    season: CreativeWorkSeason | URL | None = None
    seasons: CreativeWorkSeason | None = None
    trailer: VideoObject | None = None


@dataclass
class MovieSeries(CreativeWorkSeries):
    actor: Person | None = None
    actors: Person | None = None
    director: Person | None = None
    directors: Person | None = None
    musicBy: MusicGroup | Person | None = None
    productionCompany: Organization | None = None
    trailer: VideoObject | None = None


@dataclass
class PodcastSeries(CreativeWorkSeries):
    actor: Person | None = None
    webFeed: DataFeed | URL | None = None


@dataclass
class BookSeries(CreativeWorkSeries):
    pass


@dataclass
class Periodical(CreativeWorkSeries):
    pass


@dataclass
class ComicSeries(Periodical):
    pass


@dataclass
class Newspaper(Periodical):
    pass


@dataclass
class TVSeries(CreativeWorkSeries):
    actor: Person | None = None
    actors: Person | None = None
    containsSeason: CreativeWorkSeason | None = None
    countryOfOrigin: Country | None = None
    director: Person | None = None
    directors: Person | None = None
    episode: Episode | None = None
    episodes: Episode | None = None
    musicBy: MusicGroup | Person | None = None
    numberOfEpisodes: Integer | None = None
    numberOfSeasons: Integer | None = None
    productionCompany: Organization | None = None
    season: CreativeWorkSeason | URL | None = None
    seasons: CreativeWorkSeason | None = None
    trailer: VideoObject | None = None


@dataclass
class RecommendedDoseSchedule(DoseSchedule):
    pass


@dataclass
class ReportedDoseSchedule(DoseSchedule):
    pass


@dataclass
class MaximumDoseSchedule(DoseSchedule):
    pass


@dataclass
class LakeBodyOfWater(BodyOfWater):
    pass


@dataclass
class Waterfall(BodyOfWater):
    pass


@dataclass
class OceanBodyOfWater(BodyOfWater):
    pass


@dataclass
class Pond(BodyOfWater):
    pass


@dataclass
class Canal(BodyOfWater):
    pass


@dataclass
class RiverBodyOfWater(BodyOfWater):
    pass


@dataclass
class SeaBodyOfWater(BodyOfWater):
    pass


@dataclass
class Reservoir(BodyOfWater):
    pass


@dataclass
class Restaurant(FoodEstablishment):
    pass


@dataclass
class MensClothingStore(Store):
    pass


@dataclass
class GolfCourse(SportsActivityLocation):
    pass


@dataclass
class MovieRentalStore(Store):
    pass


@dataclass
class BikeStore(Store):
    pass


@dataclass
class MovingCompany(HomeAndConstructionBusiness):
    pass


@dataclass
class GasStation(AutomotiveBusiness):
    pass


@dataclass
class OutletStore(Store):
    pass


@dataclass
class PublicSwimmingPool(SportsActivityLocation):
    pass


@dataclass
class AutoRepair(AutomotiveBusiness):
    pass


@dataclass
class DaySpa(HealthAndBeautyBusiness):
    pass


@dataclass
class ShoeStore(Store):
    pass


@dataclass
class AutoRental(AutomotiveBusiness):
    pass


@dataclass
class MotorcycleRepair(AutomotiveBusiness):
    pass


@dataclass
class AutoWash(AutomotiveBusiness):
    pass


@dataclass
class NailSalon(HealthAndBeautyBusiness):
    pass


@dataclass
class BookStore(Store):
    pass


@dataclass
class GroceryStore(Store):
    pass


@dataclass
class SportsClub(SportsActivityLocation):
    pass


@dataclass
class PostOffice(GovernmentOffice):
    pass


@dataclass
class HobbyShop(Store):
    pass


@dataclass
class BedAndBreakfast(LodgingBusiness):
    pass


@dataclass
class PetStore(Store):
    pass


@dataclass
class HairSalon(HealthAndBeautyBusiness):
    pass


@dataclass
class Hostel(LodgingBusiness):
    pass


@dataclass
class BarOrPub(FoodEstablishment):
    pass


@dataclass
class ToyStore(Store):
    pass


@dataclass
class FastFoodRestaurant(FoodEstablishment):
    pass


@dataclass
class BowlingAlley(SportsActivityLocation):
    pass


@dataclass
class ConvenienceStore(Store):
    pass


@dataclass
class Motel(LodgingBusiness):
    pass


@dataclass
class Electrician(HomeAndConstructionBusiness):
    pass


@dataclass
class DepartmentStore(Store):
    pass


@dataclass
class Distillery(FoodEstablishment):
    pass


@dataclass
class Winery(FoodEstablishment):
    pass


@dataclass
class Notary(LegalService):
    pass


@dataclass
class InsuranceAgency(FinancialService):
    pass


@dataclass
class PawnShop(Store):
    pass


@dataclass
class Hotel(LodgingBusiness):
    pass


@dataclass
class CafeOrCoffeeShop(FoodEstablishment):
    pass


@dataclass
class ArtGallery(EntertainmentBusiness):
    pass


@dataclass
class OfficeEquipmentStore(Store):
    pass


@dataclass
class RoofingContractor(HomeAndConstructionBusiness):
    pass


@dataclass
class MobilePhoneStore(Store):
    pass


@dataclass
class IceCreamShop(FoodEstablishment):
    pass


@dataclass
class AccountingService(FinancialService):
    pass


@dataclass
class GardenStore(Store):
    pass


@dataclass
class ExerciseGym(SportsActivityLocation):
    pass


@dataclass
class Plumber(HomeAndConstructionBusiness):
    pass


@dataclass
class MotorcycleDealer(AutomotiveBusiness):
    pass


@dataclass
class Locksmith(HomeAndConstructionBusiness):
    pass


@dataclass
class Attorney(LegalService):
    pass


@dataclass
class MusicStore(Store):
    pass


@dataclass
class Resort(LodgingBusiness):
    pass


@dataclass
class SkiResort(Resort, SportsActivityLocation):
    pass


@dataclass
class BeautySalon(HealthAndBeautyBusiness):
    pass


@dataclass
class AdultEntertainment(EntertainmentBusiness):
    pass


@dataclass
class TattooParlor(HealthAndBeautyBusiness):
    pass


@dataclass
class ComputerStore(Store):
    pass


@dataclass
class HousePainter(HomeAndConstructionBusiness):
    pass


@dataclass
class AutoBodyShop(AutomotiveBusiness):
    pass


@dataclass
class AutomatedTeller(FinancialService):
    pass


@dataclass
class HardwareStore(Store):
    pass


@dataclass
class TennisComplex(SportsActivityLocation):
    pass


@dataclass
class Casino(EntertainmentBusiness):
    pass


@dataclass
class TireShop(Store):
    pass


@dataclass
class WholesaleStore(Store):
    pass


@dataclass
class ElectronicsStore(Store):
    pass


@dataclass
class AmusementPark(EntertainmentBusiness):
    pass


@dataclass
class ClothingStore(Store):
    pass


@dataclass
class SportingGoodsStore(Store):
    pass


@dataclass
class Optician(MedicalBusiness):
    pass


@dataclass
class Brewery(FoodEstablishment):
    pass


@dataclass
class Bakery(FoodEstablishment):
    pass


@dataclass
class Florist(Store):
    pass


@dataclass
class GeneralContractor(HomeAndConstructionBusiness):
    pass


@dataclass
class HomeGoodsStore(Store):
    pass


@dataclass
class JewelryStore(Store):
    pass


@dataclass
class BankOrCreditUnion(FinancialService):
    pass


@dataclass
class FurnitureStore(Store):
    pass


@dataclass
class HVACBusiness(HomeAndConstructionBusiness):
    pass


@dataclass
class ComedyClub(EntertainmentBusiness):
    pass


@dataclass
class AutoDealer(AutomotiveBusiness):
    pass


@dataclass
class LiquorStore(Store):
    pass


@dataclass
class NightClub(EntertainmentBusiness):
    pass


@dataclass
class MedicalClinic(MedicalBusiness, MedicalOrganization):
    availableService: MedicalProcedure | MedicalTest | MedicalTherapy | None = None
    medicalSpecialty: MedicalSpecialty | None = None


@dataclass
class CovidTestingFacility(MedicalClinic):
    pass


@dataclass
class Physician(MedicalBusiness, MedicalOrganization):
    availableService: MedicalProcedure | MedicalTest | MedicalTherapy | None = None
    hospitalAffiliation: Hospital | None = None
    medicalSpecialty: MedicalSpecialty | None = None


@dataclass
class Pharmacy(MedicalBusiness, MedicalOrganization):
    pass


@dataclass
class PoliceStation(CivicStructure, EmergencyService):
    pass


@dataclass
class StadiumOrArena(CivicStructure, SportsActivityLocation):
    pass


@dataclass
class Campground(CivicStructure, LodgingBusiness):
    pass


@dataclass
class MovieTheater(CivicStructure, EntertainmentBusiness):
    screenCount: float | None = None


@dataclass
class FireStation(CivicStructure, EmergencyService):
    pass


@dataclass
class Hospital(CivicStructure, EmergencyService, MedicalOrganization):
    availableService: MedicalProcedure | MedicalTest | MedicalTherapy | None = None
    healthcareReportingData: CDCPMDRecord | Dataset | None = None
    medicalSpecialty: MedicalSpecialty | None = None


@dataclass
class HealthClub(HealthAndBeautyBusiness, SportsActivityLocation):
    pass


@dataclass
class AutoPartsStore(AutomotiveBusiness, Store):
    pass


@dataclass
class Dentist(MedicalBusiness, MedicalOrganization):
    pass
