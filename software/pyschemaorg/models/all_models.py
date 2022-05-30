# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-30T18:45:47.722746
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com

from __future__ import annotations
from dataclasses import dataclass

from models.abstract_base import AbstractBase


@dataclass
class Boolean(AbstractBase):
    pass


@dataclass
class Time(AbstractBase):
    pass


@dataclass
class Thing(AbstractBase):
    additionalType: URL | None = None
    alternateName: Text | None = None
    description: Text | None = None
    disambiguatingDescription: Text | None = None
    identifier: PropertyValue | Text | URL | None = None
    image: ImageObject | URL | None = None
    mainEntityOfPage: CreativeWork | URL | None = None
    name: Text | None = None
    potentialAction: Action | None = None
    sameAs: URL | None = None
    subjectOf: CreativeWork | Event | None = None
    url: URL | None = None


@dataclass
class Person(Thing):
    additionalName: Text | None = None
    address: PostalAddress | Text | None = None
    affiliation: Organization | None = None
    alumniOf: EducationalOrganization | Organization | None = None
    award: Text | None = None
    awards: Text | None = None
    birthDate: Date | None = None
    birthPlace: Place | None = None
    brand: Brand | Organization | None = None
    callSign: Text | None = None
    children: Person | None = None
    colleague: Person | URL | None = None
    colleagues: Person | None = None
    contactPoint: ContactPoint | None = None
    contactPoints: ContactPoint | None = None
    deathDate: Date | None = None
    deathPlace: Place | None = None
    duns: Text | None = None
    email: Text | None = None
    familyName: Text | None = None
    faxNumber: Text | None = None
    follows: Person | None = None
    funder: Organization | Person | None = None
    funding: Grant | None = None
    gender: GenderType | Text | None = None
    givenName: Text | None = None
    globalLocationNumber: Text | None = None
    hasCredential: EducationalOccupationalCredential | None = None
    hasOccupation: Occupation | None = None
    hasOfferCatalog: OfferCatalog | None = None
    hasPOS: Place | None = None
    height: Distance | QuantitativeValue | None = None
    homeLocation: ContactPoint | Place | None = None
    honorificPrefix: Text | None = None
    honorificSuffix: Text | None = None
    interactionStatistic: InteractionCounter | None = None
    isicV4: Text | None = None
    jobTitle: DefinedTerm | Text | None = None
    knows: Person | None = None
    knowsAbout: Text | Thing | URL | None = None
    knowsLanguage: Language | Text | None = None
    makesOffer: Offer | None = None
    memberOf: Organization | ProgramMembership | None = None
    naics: Text | None = None
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
    taxID: Text | None = None
    telephone: Text | None = None
    vatID: Text | None = None
    weight: QuantitativeValue | None = None
    workLocation: ContactPoint | Place | None = None
    worksFor: Organization | None = None


@dataclass
class Taxon(Thing):
    childTaxon: Taxon | Text | URL | None = None
    hasDefinedTerm: DefinedTerm | None = None
    parentTaxon: Taxon | Text | URL | None = None
    taxonRank: PropertyValue | Text | URL | None = None


@dataclass
class CreativeWork(Thing):
    about: Thing | None = None
    abstract: Text | None = None
    accessMode: Text | None = None
    accessModeSufficient: ItemList | None = None
    accessibilityAPI: Text | None = None
    accessibilityControl: Text | None = None
    accessibilityFeature: Text | None = None
    accessibilityHazard: Text | None = None
    accessibilitySummary: Text | None = None
    accountablePerson: Person | None = None
    acquireLicensePage: CreativeWork | URL | None = None
    aggregateRating: AggregateRating | None = None
    alternativeHeadline: Text | None = None
    archivedAt: URL | WebPage | None = None
    assesses: DefinedTerm | Text | None = None
    associatedMedia: MediaObject | None = None
    audience: Audience | None = None
    audio: AudioObject | Clip | MusicRecording | None = None
    author: Organization | Person | None = None
    award: Text | None = None
    awards: Text | None = None
    character: Person | None = None
    citation: CreativeWork | Text | None = None
    comment: Comment | None = None
    commentCount: Integer | None = None
    conditionsOfAccess: Text | None = None
    contentLocation: Place | None = None
    contentRating: Rating | Text | None = None
    contentReferenceTime: DateTime | None = None
    contributor: Organization | Person | None = None
    copyrightHolder: Organization | Person | None = None
    copyrightNotice: Text | None = None
    copyrightYear: Number | None = None
    correction: CorrectionComment | Text | URL | None = None
    countryOfOrigin: Country | None = None
    creativeWorkStatus: DefinedTerm | Text | None = None
    creator: Organization | Person | None = None
    creditText: Text | None = None
    dateCreated: Date | DateTime | None = None
    dateModified: Date | DateTime | None = None
    datePublished: Date | DateTime | None = None
    discussionUrl: URL | None = None
    editEIDR: Text | URL | None = None
    editor: Person | None = None
    educationalAlignment: AlignmentObject | None = None
    educationalLevel: DefinedTerm | Text | URL | None = None
    educationalUse: DefinedTerm | Text | None = None
    encoding: MediaObject | None = None
    encodingFormat: Text | URL | None = None
    encodings: MediaObject | None = None
    exampleOfWork: CreativeWork | None = None
    expires: Date | None = None
    fileFormat: Text | URL | None = None
    funder: Organization | Person | None = None
    funding: Grant | None = None
    genre: Text | URL | None = None
    hasPart: CreativeWork | None = None
    headline: Text | None = None
    inLanguage: Language | Text | None = None
    interactionStatistic: InteractionCounter | None = None
    interactivityType: Text | None = None
    interpretedAsClaim: Claim | None = None
    isAccessibleForFree: Boolean | None = None
    isBasedOn: CreativeWork | Product | URL | None = None
    isBasedOnUrl: CreativeWork | Product | URL | None = None
    isFamilyFriendly: Boolean | None = None
    isPartOf: CreativeWork | URL | None = None
    keywords: DefinedTerm | Text | URL | None = None
    learningResourceType: DefinedTerm | Text | None = None
    license: CreativeWork | URL | None = None
    locationCreated: Place | None = None
    mainEntity: Thing | None = None
    maintainer: Organization | Person | None = None
    material: Product | Text | URL | None = None
    materialExtent: QuantitativeValue | Text | None = None
    mentions: Thing | None = None
    offers: Demand | Offer | None = None
    pattern: DefinedTerm | Text | None = None
    position: Integer | Text | None = None
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
    schemaVersion: Text | URL | None = None
    sdDatePublished: Date | None = None
    sdLicense: CreativeWork | URL | None = None
    sdPublisher: Organization | Person | None = None
    size: DefinedTerm | QuantitativeValue | SizeSpecification | Text | None = None
    sourceOrganization: Organization | None = None
    spatial: Place | None = None
    spatialCoverage: Place | None = None
    sponsor: Organization | Person | None = None
    teaches: DefinedTerm | Text | None = None
    temporal: DateTime | Text | None = None
    temporalCoverage: DateTime | Text | URL | None = None
    text: Text | None = None
    thumbnailUrl: URL | None = None
    timeRequired: Duration | None = None
    translationOfWork: CreativeWork | None = None
    translator: Organization | Person | None = None
    typicalAgeRange: Text | None = None
    usageInfo: CreativeWork | URL | None = None
    version: Number | Text | None = None
    video: Clip | VideoObject | None = None
    workExample: CreativeWork | None = None
    workTranslation: CreativeWork | None = None


@dataclass
class Product(Thing):
    additionalProperty: PropertyValue | None = None
    aggregateRating: AggregateRating | None = None
    audience: Audience | None = None
    award: Text | None = None
    awards: Text | None = None
    brand: Brand | Organization | None = None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None = None
    color: Text | None = None
    countryOfAssembly: Text | None = None
    countryOfLastProcessing: Text | None = None
    countryOfOrigin: Country | None = None
    depth: Distance | QuantitativeValue | None = None
    funding: Grant | None = None
    gtin: Text | None = None
    gtin12: Text | None = None
    gtin13: Text | None = None
    gtin14: Text | None = None
    gtin8: Text | None = None
    hasAdultConsideration: AdultOrientedEnumeration | None = None
    hasEnergyConsumptionDetails: EnergyConsumptionDetails | None = None
    hasMeasurement: QuantitativeValue | None = None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None = None
    hasProductReturnPolicy: ProductReturnPolicy | None = None
    height: Distance | QuantitativeValue | None = None
    inProductGroupWithID: Text | None = None
    isAccessoryOrSparePartFor: Product | None = None
    isConsumableFor: Product | None = None
    isFamilyFriendly: Boolean | None = None
    isRelatedTo: Product | Service | None = None
    isSimilarTo: Product | Service | None = None
    isVariantOf: ProductGroup | ProductModel | None = None
    itemCondition: OfferItemCondition | None = None
    keywords: DefinedTerm | Text | URL | None = None
    logo: ImageObject | URL | None = None
    manufacturer: Organization | None = None
    material: Product | Text | URL | None = None
    model: ProductModel | Text | None = None
    mpn: Text | None = None
    nsn: Text | None = None
    offers: Demand | Offer | None = None
    pattern: DefinedTerm | Text | None = None
    productID: Text | None = None
    productionDate: Date | None = None
    purchaseDate: Date | None = None
    releaseDate: Date | None = None
    review: Review | None = None
    reviews: Review | None = None
    size: DefinedTerm | QuantitativeValue | SizeSpecification | Text | None = None
    sku: Text | None = None
    slogan: Text | None = None
    weight: QuantitativeValue | None = None
    width: Distance | QuantitativeValue | None = None


@dataclass
class Organization(Thing):
    actionableFeedbackPolicy: CreativeWork | URL | None = None
    address: PostalAddress | Text | None = None
    aggregateRating: AggregateRating | None = None
    alumni: Person | None = None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None = None
    award: Text | None = None
    awards: Text | None = None
    brand: Brand | Organization | None = None
    contactPoint: ContactPoint | None = None
    contactPoints: ContactPoint | None = None
    correctionsPolicy: CreativeWork | URL | None = None
    department: Organization | None = None
    dissolutionDate: Date | None = None
    diversityPolicy: CreativeWork | URL | None = None
    diversityStaffingReport: Article | URL | None = None
    duns: Text | None = None
    email: Text | None = None
    employee: Person | None = None
    employees: Person | None = None
    ethicsPolicy: CreativeWork | URL | None = None
    event: Event | None = None
    events: Event | None = None
    faxNumber: Text | None = None
    founder: Person | None = None
    founders: Person | None = None
    foundingDate: Date | None = None
    foundingLocation: Place | None = None
    funder: Organization | Person | None = None
    funding: Grant | None = None
    globalLocationNumber: Text | None = None
    hasCredential: EducationalOccupationalCredential | None = None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None = None
    hasOfferCatalog: OfferCatalog | None = None
    hasPOS: Place | None = None
    hasProductReturnPolicy: ProductReturnPolicy | None = None
    interactionStatistic: InteractionCounter | None = None
    isicV4: Text | None = None
    iso6523Code: Text | None = None
    keywords: DefinedTerm | Text | URL | None = None
    knowsAbout: Text | Thing | URL | None = None
    knowsLanguage: Language | Text | None = None
    legalName: Text | None = None
    leiCode: Text | None = None
    location: Place | PostalAddress | Text | VirtualLocation | None = None
    logo: ImageObject | URL | None = None
    makesOffer: Offer | None = None
    member: Organization | Person | None = None
    memberOf: Organization | ProgramMembership | None = None
    members: Organization | Person | None = None
    naics: Text | None = None
    nonprofitStatus: NonprofitType | None = None
    numberOfEmployees: QuantitativeValue | None = None
    ownershipFundingInfo: AboutPage | CreativeWork | Text | URL | None = None
    owns: OwnershipInfo | Product | None = None
    parentOrganization: Organization | None = None
    publishingPrinciples: CreativeWork | URL | None = None
    review: Review | None = None
    reviews: Review | None = None
    seeks: Demand | None = None
    serviceArea: AdministrativeArea | GeoShape | Place | None = None
    slogan: Text | None = None
    sponsor: Organization | Person | None = None
    subOrganization: Organization | None = None
    taxID: Text | None = None
    telephone: Text | None = None
    unnamedSourcesPolicy: CreativeWork | URL | None = None
    vatID: Text | None = None


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
    doorTime: DateTime | Time | None = None
    duration: Duration | None = None
    endDate: Date | DateTime | None = None
    eventAttendanceMode: EventAttendanceModeEnumeration | None = None
    eventSchedule: Schedule | None = None
    eventStatus: EventStatusType | None = None
    funder: Organization | Person | None = None
    funding: Grant | None = None
    inLanguage: Language | Text | None = None
    isAccessibleForFree: Boolean | None = None
    keywords: DefinedTerm | Text | URL | None = None
    location: Place | PostalAddress | Text | VirtualLocation | None = None
    maximumAttendeeCapacity: Integer | None = None
    maximumPhysicalAttendeeCapacity: Integer | None = None
    maximumVirtualAttendeeCapacity: Integer | None = None
    offers: Demand | Offer | None = None
    organizer: Organization | Person | None = None
    performer: Organization | Person | None = None
    performers: Organization | Person | None = None
    previousStartDate: Date | None = None
    recordedIn: CreativeWork | None = None
    remainingAttendeeCapacity: Integer | None = None
    review: Review | None = None
    sponsor: Organization | Person | None = None
    startDate: Date | DateTime | None = None
    subEvent: Event | None = None
    subEvents: Event | None = None
    superEvent: Event | None = None
    translator: Organization | Person | None = None
    typicalAgeRange: Text | None = None
    workFeatured: CreativeWork | None = None
    workPerformed: CreativeWork | None = None


@dataclass
class MedicalEntity(Thing):
    code: MedicalCode | None = None
    funding: Grant | None = None
    guideline: MedicalGuideline | None = None
    legalStatus: DrugLegalStatus | MedicalEnumeration | Text | None = None
    medicineSystem: MedicineSystem | None = None
    recognizingAuthority: Organization | None = None
    relevantSpecialty: MedicalSpecialty | None = None
    study: MedicalStudy | None = None


@dataclass
class Place(Thing):
    additionalProperty: PropertyValue | None = None
    address: PostalAddress | Text | None = None
    aggregateRating: AggregateRating | None = None
    amenityFeature: LocationFeatureSpecification | None = None
    branchCode: Text | None = None
    containedIn: Place | None = None
    containedInPlace: Place | None = None
    containsPlace: Place | None = None
    event: Event | None = None
    events: Event | None = None
    faxNumber: Text | None = None
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
    globalLocationNumber: Text | None = None
    hasDriveThroughService: Boolean | None = None
    hasMap: Map | URL | None = None
    isAccessibleForFree: Boolean | None = None
    isicV4: Text | None = None
    keywords: DefinedTerm | Text | URL | None = None
    latitude: Number | Text | None = None
    logo: ImageObject | URL | None = None
    longitude: Number | Text | None = None
    map: URL | None = None
    maps: URL | None = None
    maximumAttendeeCapacity: Integer | None = None
    openingHoursSpecification: OpeningHoursSpecification | None = None
    photo: ImageObject | Photograph | None = None
    photos: ImageObject | Photograph | None = None
    publicAccess: Boolean | None = None
    review: Review | None = None
    reviews: Review | None = None
    slogan: Text | None = None
    smokingAllowed: Boolean | None = None
    specialOpeningHoursSpecification: OpeningHoursSpecification | None = None
    telephone: Text | None = None
    tourBookingPage: URL | None = None


@dataclass
class Action(Thing):
    actionStatus: ActionStatusType | None = None
    agent: Organization | Person | None = None
    endTime: DateTime | Time | None = None
    error: Thing | None = None
    instrument: Thing | None = None
    location: Place | PostalAddress | Text | VirtualLocation | None = None
    object: Thing | None = None
    participant: Organization | Person | None = None
    provider: Organization | Person | None = None
    result: Thing | None = None
    startTime: DateTime | Time | None = None
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
    hasRepresentation: PropertyValue | Text | URL | None = None
    isEncodedByBioChemEntity: Gene | None = None
    isInvolvedInBiologicalProcess: DefinedTerm | PropertyValue | URL | None = None
    isLocatedInSubcellularLocation: DefinedTerm | PropertyValue | URL | None = None
    isPartOfBioChemEntity: BioChemEntity | None = None
    taxonomicRange: DefinedTerm | Taxon | Text | URL | None = None


@dataclass
class Intangible(Thing):
    pass


@dataclass
class StupidType(Thing):
    stupidProperty: QuantitativeValue | None = None


@dataclass
class Date(AbstractBase):
    pass


@dataclass
class DateTime(AbstractBase):
    pass


@dataclass
class DataType(AbstractBase):
    pass


@dataclass
class Number(AbstractBase):
    pass


@dataclass
class Integer(Number):
    pass


@dataclass
class Float(Number):
    pass


@dataclass
class Text(AbstractBase):
    pass


@dataclass
class URL(Text):
    pass


@dataclass
class PronounceableText(Text):
    inLanguage: Language | Text | None = None
    phoneticText: Text | None = None
    speechToTextMarkup: Text | None = None
    textValue: Text | None = None


@dataclass
class CssSelectorType(Text):
    pass


@dataclass
class XPathType(Text):
    pass


@dataclass
class Accommodation(Place):
    accommodationCategory: Text | None = None
    accommodationFloorPlan: FloorPlan | None = None
    amenityFeature: LocationFeatureSpecification | None = None
    floorLevel: Text | None = None
    floorSize: QuantitativeValue | None = None
    leaseLength: Duration | QuantitativeValue | None = None
    numberOfBathroomsTotal: Integer | None = None
    numberOfBedrooms: Number | QuantitativeValue | None = None
    numberOfFullBathrooms: Number | None = None
    numberOfPartialBathrooms: Number | None = None
    numberOfRooms: Number | QuantitativeValue | None = None
    permittedUsage: Text | None = None
    petsAllowed: Boolean | Text | None = None
    tourBookingPage: URL | None = None
    yearBuilt: Number | None = None


@dataclass
class Apartment(Accommodation):
    numberOfRooms: Number | QuantitativeValue | None = None
    occupancy: QuantitativeValue | None = None


@dataclass
class House(Accommodation):
    numberOfRooms: Number | QuantitativeValue | None = None


@dataclass
class Suite(Accommodation):
    bed: BedDetails | BedType | Text | None = None
    numberOfRooms: Number | QuantitativeValue | None = None
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
    isrcCode: Text | None = None
    recordingOf: MusicComposition | None = None


@dataclass
class ParcelDelivery(Intangible):
    carrier: Organization | None = None
    deliveryAddress: PostalAddress | None = None
    deliveryStatus: DeliveryEvent | None = None
    expectedArrivalFrom: Date | DateTime | None = None
    expectedArrivalUntil: Date | DateTime | None = None
    hasDeliveryMethod: DeliveryMethod | None = None
    itemShipped: Product | None = None
    originAddress: PostalAddress | None = None
    partOfOrder: Order | None = None
    provider: Organization | Person | None = None
    trackingNumber: Text | None = None
    trackingUrl: URL | None = None


@dataclass
class Book(CreativeWork):
    abridged: Boolean | None = None
    bookEdition: Text | None = None
    bookFormat: BookFormatType | None = None
    illustrator: Person | None = None
    isbn: Text | None = None
    numberOfPages: Integer | None = None


@dataclass
class Dataset(CreativeWork):
    catalog: DataCatalog | None = None
    datasetTimeInterval: DateTime | None = None
    distribution: DataDownload | None = None
    includedDataCatalog: DataCatalog | None = None
    includedInDataCatalog: DataCatalog | None = None
    issn: Text | None = None
    measurementTechnique: Text | URL | None = None
    variableMeasured: PropertyValue | Text | None = None
    variablesMeasured: PropertyValue | Text | None = None


@dataclass
class DataFeed(Dataset):
    dataFeedElement: DataFeedItem | Text | Thing | None = None


@dataclass
class MediaObject(CreativeWork):
    associatedArticle: NewsArticle | None = None
    bitrate: Text | None = None
    contentSize: Text | None = None
    contentUrl: URL | None = None
    duration: Duration | None = None
    embedUrl: URL | None = None
    encodesCreativeWork: CreativeWork | None = None
    encodingFormat: Text | URL | None = None
    endTime: DateTime | Time | None = None
    height: Distance | QuantitativeValue | None = None
    ineligibleRegion: GeoShape | Place | Text | None = None
    interpretedAsClaim: Claim | None = None
    playerType: Text | None = None
    productionCompany: Organization | None = None
    regionsAllowed: Place | None = None
    requiresSubscription: Boolean | MediaSubscription | None = None
    sha256: Text | None = None
    startTime: DateTime | Time | None = None
    uploadDate: Date | None = None
    width: Distance | QuantitativeValue | None = None


@dataclass
class AudioObject(MediaObject):
    caption: MediaObject | Text | None = None
    embeddedTextCaption: Text | None = None
    transcript: Text | None = None


@dataclass
class ImageObject(MediaObject):
    caption: MediaObject | Text | None = None
    embeddedTextCaption: Text | None = None
    exifData: PropertyValue | Text | None = None
    representativeOfPage: Boolean | None = None
    thumbnail: ImageObject | None = None


@dataclass
class VideoObject(MediaObject):
    actor: Person | None = None
    actors: Person | None = None
    caption: MediaObject | Text | None = None
    director: Person | None = None
    directors: Person | None = None
    embeddedTextCaption: Text | None = None
    musicBy: MusicGroup | Person | None = None
    thumbnail: ImageObject | None = None
    transcript: Text | None = None
    videoFrameSize: Text | None = None
    videoQuality: Text | None = None


@dataclass
class d_3DModel(MediaObject):
    isResizable: Boolean | None = None


@dataclass
class MusicVideoObject(MediaObject):
    pass


@dataclass
class DataDownload(MediaObject):
    measurementTechnique: Text | URL | None = None


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
    baseSalary: MonetaryAmount | Number | PriceSpecification | None = None
    benefits: Text | None = None
    datePosted: Date | DateTime | None = None
    directApply: Boolean | None = None
    educationRequirements: EducationalOccupationalCredential | Text | None = None
    eligibilityToWorkRequirement: Text | None = None
    employerOverview: Text | None = None
    employmentType: Text | None = None
    employmentUnit: Organization | None = None
    estimatedSalary: MonetaryAmount | MonetaryAmountDistribution | Number | None = None
    experienceInPlaceOfEducation: Boolean | None = None
    experienceRequirements: OccupationalExperienceRequirements | Text | None = None
    hiringOrganization: Organization | None = None
    incentiveCompensation: Text | None = None
    incentives: Text | None = None
    industry: DefinedTerm | Text | None = None
    jobBenefits: Text | None = None
    jobImmediateStart: Boolean | None = None
    jobLocation: Place | None = None
    jobLocationType: Text | None = None
    jobStartDate: Date | Text | None = None
    occupationalCategory: CategoryCode | Text | None = None
    physicalRequirement: DefinedTerm | Text | URL | None = None
    qualifications: EducationalOccupationalCredential | Text | None = None
    relevantOccupation: Occupation | None = None
    responsibilities: Text | None = None
    salaryCurrency: Text | None = None
    securityClearanceRequirement: Text | URL | None = None
    sensoryRequirement: DefinedTerm | Text | URL | None = None
    skills: DefinedTerm | Text | None = None
    specialCommitments: Text | None = None
    title: Text | None = None
    totalJobOpenings: Integer | None = None
    validThrough: Date | DateTime | None = None
    workHours: Text | None = None


@dataclass
class MedicalOrganization(Organization):
    healthPlanNetworkId: Text | None = None
    isAcceptingNewPatients: Boolean | None = None
    medicalSpecialty: MedicalSpecialty | None = None


@dataclass
class DiagnosticLab(MedicalOrganization):
    availableTest: MedicalTest | None = None


@dataclass
class VeterinaryCare(MedicalOrganization):
    pass


@dataclass
class MedicalProcedure(MedicalEntity):
    bodyLocation: Text | None = None
    followup: Text | None = None
    howPerformed: Text | None = None
    preparation: MedicalEntity | Text | None = None
    procedureType: MedicalProcedureType | None = None
    status: EventStatusType | MedicalStudyStatus | Text | None = None


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
    applicationCategory: Text | URL | None = None
    applicationSubCategory: Text | URL | None = None
    applicationSuite: Text | None = None
    availableOnDevice: Text | None = None
    countriesNotSupported: Text | None = None
    countriesSupported: Text | None = None
    device: Text | None = None
    downloadUrl: URL | None = None
    featureList: Text | URL | None = None
    fileSize: Text | None = None
    installUrl: URL | None = None
    memoryRequirements: Text | URL | None = None
    operatingSystem: Text | None = None
    permissions: Text | None = None
    processorRequirements: Text | None = None
    releaseNotes: Text | URL | None = None
    requirements: Text | URL | None = None
    screenshot: ImageObject | URL | None = None
    softwareAddOn: SoftwareApplication | None = None
    softwareHelp: CreativeWork | None = None
    softwareRequirements: Text | URL | None = None
    softwareVersion: Text | None = None
    storageRequirements: Text | URL | None = None
    supportingData: DataFeed | None = None


@dataclass
class WebApplication(SoftwareApplication):
    browserRequirements: Text | None = None


@dataclass
class MobileApplication(SoftwareApplication):
    carrierRequirements: Text | None = None


@dataclass
class MerchantReturnPolicy(Intangible):
    additionalProperty: PropertyValue | None = None
    applicableCountry: Country | Text | None = None
    customerRemorseReturnFees: ReturnFeesEnumeration | None = None
    customerRemorseReturnLabelSource: ReturnLabelSourceEnumeration | None = None
    customerRemorseReturnShippingFeesAmount: MonetaryAmount | None = None
    inStoreReturnsOffered: Boolean | None = None
    itemCondition: OfferItemCondition | None = None
    itemDefectReturnFees: ReturnFeesEnumeration | None = None
    itemDefectReturnLabelSource: ReturnLabelSourceEnumeration | None = None
    itemDefectReturnShippingFeesAmount: MonetaryAmount | None = None
    merchantReturnDays: Date | DateTime | Integer | None = None
    merchantReturnLink: URL | None = None
    refundType: RefundTypeEnumeration | None = None
    restockingFee: MonetaryAmount | Number | None = None
    returnFees: ReturnFeesEnumeration | None = None
    returnLabelSource: ReturnLabelSourceEnumeration | None = None
    returnMethod: ReturnMethodEnumeration | None = None
    returnPolicyCategory: MerchantReturnEnumeration | None = None
    returnPolicyCountry: Country | Text | None = None
    returnPolicySeasonalOverride: MerchantReturnPolicySeasonalOverride | None = None
    returnShippingFeesAmount: MonetaryAmount | None = None


@dataclass
class MerchantReturnPolicySeasonalOverride(Intangible):
    endDate: Date | DateTime | None = None
    merchantReturnDays: Date | DateTime | Integer | None = None
    returnPolicyCategory: MerchantReturnEnumeration | None = None
    startDate: Date | DateTime | None = None


@dataclass
class WebPage(CreativeWork):
    breadcrumb: BreadcrumbList | Text | None = None
    lastReviewed: Date | None = None
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
    datePosted: Date | DateTime | None = None
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
    aspect: Text | None = None
    medicalAudience: MedicalAudience | MedicalAudienceType | None = None


@dataclass
class ItemPage(WebPage):
    pass


@dataclass
class Festival(Event):
    pass


@dataclass
class Invoice(Intangible):
    accountId: Text | None = None
    billingPeriod: Duration | None = None
    broker: Organization | Person | None = None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None = None
    confirmationNumber: Text | None = None
    customer: Organization | Person | None = None
    minimumPaymentDue: MonetaryAmount | PriceSpecification | None = None
    paymentDue: DateTime | None = None
    paymentDueDate: Date | DateTime | None = None
    paymentMethod: PaymentMethod | None = None
    paymentMethodId: Text | None = None
    paymentStatus: PaymentStatusType | Text | None = None
    provider: Organization | Person | None = None
    referencesOrder: Order | None = None
    scheduledPaymentDate: Date | None = None
    totalPaymentDue: MonetaryAmount | PriceSpecification | None = None


@dataclass
class HealthPlanNetwork(Intangible):
    healthPlanCostSharing: Boolean | None = None
    healthPlanNetworkId: Text | None = None
    healthPlanNetworkTier: Text | None = None


@dataclass
class SportsEvent(Event):
    awayTeam: Person | SportsTeam | None = None
    competitor: Person | SportsTeam | None = None
    homeTeam: Person | SportsTeam | None = None
    sport: Text | URL | None = None


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
    healthPlanCoinsuranceOption: Text | None = None
    healthPlanCoinsuranceRate: Number | None = None
    healthPlanCopay: PriceSpecification | None = None
    healthPlanCopayOption: Text | None = None
    healthPlanPharmacyCategory: Text | None = None


@dataclass
class EducationEvent(Event):
    assesses: DefinedTerm | Text | None = None
    educationalLevel: DefinedTerm | Text | URL | None = None
    teaches: DefinedTerm | Text | None = None


@dataclass
class LearningResource(CreativeWork):
    assesses: DefinedTerm | Text | None = None
    competencyRequired: DefinedTerm | Text | URL | None = None
    educationalAlignment: AlignmentObject | None = None
    educationalLevel: DefinedTerm | Text | URL | None = None
    educationalUse: DefinedTerm | Text | None = None
    learningResourceType: DefinedTerm | Text | None = None
    teaches: DefinedTerm | Text | None = None


@dataclass
class Course(LearningResource):
    courseCode: Text | None = None
    coursePrerequisites: AlignmentObject | Course | Text | None = None
    educationalCredentialAwarded: EducationalOccupationalCredential | Text | URL | None = None
    hasCourseInstance: CourseInstance | None = None
    numberOfCredits: Integer | StructuredValue | None = None
    occupationalCredentialAwarded: EducationalOccupationalCredential | Text | URL | None = None


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
    exerciseType: Text | None = None
    fromLocation: Place | None = None
    opponent: Person | None = None
    sportsActivityLocation: SportsActivityLocation | None = None
    sportsEvent: SportsEvent | None = None
    sportsTeam: SportsTeam | None = None
    toLocation: Place | None = None


@dataclass
class Reservation(Intangible):
    bookingAgent: Organization | Person | None = None
    bookingTime: DateTime | None = None
    broker: Organization | Person | None = None
    modifiedTime: DateTime | None = None
    priceCurrency: Text | None = None
    programMembershipUsed: ProgramMembership | None = None
    provider: Organization | Person | None = None
    reservationFor: Thing | None = None
    reservationId: Text | None = None
    reservationStatus: ReservationStatusType | None = None
    reservedTicket: Ticket | None = None
    totalPrice: Number | PriceSpecification | Text | None = None
    underName: Organization | Person | None = None


@dataclass
class FlightReservation(Reservation):
    boardingGroup: Text | None = None
    passengerPriorityStatus: QualitativeValue | Text | None = None
    passengerSequenceNumber: Text | None = None
    securityScreening: Text | None = None


@dataclass
class LodgingReservation(Reservation):
    checkinTime: DateTime | Time | None = None
    checkoutTime: DateTime | Time | None = None
    lodgingUnitDescription: Text | None = None
    lodgingUnitType: QualitativeValue | Text | None = None
    numAdults: Integer | QuantitativeValue | None = None
    numChildren: Integer | QuantitativeValue | None = None


@dataclass
class BoatReservation(Reservation):
    pass


@dataclass
class TaxiReservation(Reservation):
    partySize: Integer | QuantitativeValue | None = None
    pickupLocation: Place | None = None
    pickupTime: DateTime | None = None


@dataclass
class FoodEstablishmentReservation(Reservation):
    endTime: DateTime | Time | None = None
    partySize: Integer | QuantitativeValue | None = None
    startTime: DateTime | Time | None = None


@dataclass
class BusReservation(Reservation):
    pass


@dataclass
class ReservationPackage(Reservation):
    subReservation: Reservation | None = None


@dataclass
class RentalCarReservation(Reservation):
    dropoffLocation: Place | None = None
    dropoffTime: DateTime | None = None
    pickupLocation: Place | None = None
    pickupTime: DateTime | None = None


@dataclass
class TrainReservation(Reservation):
    pass


@dataclass
class EventReservation(Reservation):
    pass


@dataclass
class Vehicle(Product):
    accelerationTime: QuantitativeValue | None = None
    bodyType: QualitativeValue | Text | URL | None = None
    callSign: Text | None = None
    cargoVolume: QuantitativeValue | None = None
    dateVehicleFirstRegistered: Date | None = None
    driveWheelConfiguration: DriveWheelConfigurationValue | Text | None = None
    emissionsCO2: Number | None = None
    fuelCapacity: QuantitativeValue | None = None
    fuelConsumption: QuantitativeValue | None = None
    fuelEfficiency: QuantitativeValue | None = None
    fuelType: QualitativeValue | Text | URL | None = None
    knownVehicleDamages: Text | None = None
    meetsEmissionStandard: QualitativeValue | Text | URL | None = None
    mileageFromOdometer: QuantitativeValue | None = None
    modelDate: Date | None = None
    numberOfAirbags: Number | Text | None = None
    numberOfAxles: Number | QuantitativeValue | None = None
    numberOfDoors: Number | QuantitativeValue | None = None
    numberOfForwardGears: Number | QuantitativeValue | None = None
    numberOfPreviousOwners: Number | QuantitativeValue | None = None
    payload: QuantitativeValue | None = None
    productionDate: Date | None = None
    purchaseDate: Date | None = None
    seatingCapacity: Number | QuantitativeValue | None = None
    speed: QuantitativeValue | None = None
    steeringPosition: SteeringPositionValue | None = None
    stupidProperty: QuantitativeValue | None = None
    tongueWeight: QuantitativeValue | None = None
    trailerWeight: QuantitativeValue | None = None
    vehicleConfiguration: Text | None = None
    vehicleEngine: EngineSpecification | None = None
    vehicleIdentificationNumber: Text | None = None
    vehicleInteriorColor: Text | None = None
    vehicleInteriorType: Text | None = None
    vehicleModelDate: Date | None = None
    vehicleSeatingCapacity: Number | QuantitativeValue | None = None
    vehicleSpecialUsage: CarUsageType | Text | None = None
    vehicleTransmission: QualitativeValue | Text | URL | None = None
    weightTotal: QuantitativeValue | None = None
    wheelbase: QuantitativeValue | None = None


@dataclass
class Car(Vehicle):
    acrissCode: Text | None = None
    roofLoad: QuantitativeValue | None = None


@dataclass
class BusOrCoach(Vehicle):
    acrissCode: Text | None = None
    roofLoad: QuantitativeValue | None = None


@dataclass
class MotorizedBicycle(Vehicle):
    pass


@dataclass
class Motorcycle(Vehicle):
    pass


@dataclass
class EducationalOccupationalProgram(Intangible):
    applicationDeadline: Date | None = None
    applicationStartDate: Date | None = None
    dayOfWeek: DayOfWeek | None = None
    educationalCredentialAwarded: EducationalOccupationalCredential | Text | URL | None = None
    educationalProgramMode: Text | URL | None = None
    endDate: Date | DateTime | None = None
    financialAidEligible: DefinedTerm | Text | None = None
    hasCourse: Course | None = None
    maximumEnrollment: Integer | None = None
    numberOfCredits: Integer | StructuredValue | None = None
    occupationalCategory: CategoryCode | Text | None = None
    occupationalCredentialAwarded: EducationalOccupationalCredential | Text | URL | None = None
    offers: Demand | Offer | None = None
    programPrerequisites: AlignmentObject | Course | EducationalOccupationalCredential | Text | None = None
    programType: DefinedTerm | Text | None = None
    provider: Organization | Person | None = None
    salaryUponCompletion: MonetaryAmountDistribution | None = None
    startDate: Date | DateTime | None = None
    termDuration: Duration | None = None
    termsPerYear: Number | None = None
    timeOfDay: Text | None = None
    timeToComplete: Duration | None = None
    trainingSalary: MonetaryAmountDistribution | None = None
    typicalCreditsPerTerm: Integer | StructuredValue | None = None


@dataclass
class WorkBasedProgram(EducationalOccupationalProgram):
    occupationalCategory: CategoryCode | Text | None = None
    trainingSalary: MonetaryAmountDistribution | None = None


@dataclass
class EducationalOccupationalCredential(CreativeWork):
    competencyRequired: DefinedTerm | Text | URL | None = None
    credentialCategory: DefinedTerm | Text | URL | None = None
    educationalLevel: DefinedTerm | Text | URL | None = None
    recognizedBy: Organization | None = None
    validFor: Duration | None = None
    validIn: AdministrativeArea | None = None


@dataclass
class Offer(Intangible):
    acceptedPaymentMethod: LoanOrCredit | PaymentMethod | None = None
    addOn: Offer | None = None
    advanceBookingRequirement: QuantitativeValue | None = None
    aggregateRating: AggregateRating | None = None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None = None
    availability: ItemAvailability | None = None
    availabilityEnds: Date | DateTime | Time | None = None
    availabilityStarts: Date | DateTime | Time | None = None
    availableAtOrFrom: Place | None = None
    availableDeliveryMethod: DeliveryMethod | None = None
    businessFunction: BusinessFunction | None = None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None = None
    deliveryLeadTime: QuantitativeValue | None = None
    eligibleCustomerType: BusinessEntityType | None = None
    eligibleDuration: QuantitativeValue | None = None
    eligibleQuantity: QuantitativeValue | None = None
    eligibleRegion: GeoShape | Place | Text | None = None
    eligibleTransactionVolume: PriceSpecification | None = None
    gtin: Text | None = None
    gtin12: Text | None = None
    gtin13: Text | None = None
    gtin14: Text | None = None
    gtin8: Text | None = None
    hasAdultConsideration: AdultOrientedEnumeration | None = None
    hasMeasurement: QuantitativeValue | None = None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None = None
    includesObject: TypeAndQuantityNode | None = None
    ineligibleRegion: GeoShape | Place | Text | None = None
    inventoryLevel: QuantitativeValue | None = None
    isFamilyFriendly: Boolean | None = None
    itemCondition: OfferItemCondition | None = None
    itemOffered: AggregateOffer | CreativeWork | Event | MenuItem | Product | Service | Trip | None = None
    leaseLength: Duration | QuantitativeValue | None = None
    mpn: Text | None = None
    offeredBy: Organization | Person | None = None
    price: Number | Text | None = None
    priceCurrency: Text | None = None
    priceSpecification: PriceSpecification | None = None
    priceValidUntil: Date | None = None
    review: Review | None = None
    reviews: Review | None = None
    seller: Organization | Person | None = None
    serialNumber: Text | None = None
    shippingDetails: OfferShippingDetails | None = None
    sku: Text | None = None
    validFrom: Date | DateTime | None = None
    validThrough: Date | DateTime | None = None
    warranty: WarrantyPromise | None = None


@dataclass
class OfferForLease(Offer):
    pass


@dataclass
class AggregateOffer(Offer):
    highPrice: Number | Text | None = None
    lowPrice: Number | Text | None = None
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
    validFrom: Date | DateTime | None = None
    validIn: AdministrativeArea | None = None
    validUntil: Date | None = None


@dataclass
class GovernmentPermit(Permit):
    pass


@dataclass
class SoftwareSourceCode(CreativeWork):
    codeRepository: URL | None = None
    codeSampleType: Text | None = None
    programmingLanguage: ComputerLanguage | Text | None = None
    runtime: Text | None = None
    runtimePlatform: Text | None = None
    sampleType: Text | None = None
    targetProduct: SoftwareApplication | None = None


@dataclass
class Brand(Intangible):
    aggregateRating: AggregateRating | None = None
    logo: ImageObject | URL | None = None
    review: Review | None = None
    slogan: Text | None = None


@dataclass
class Occupation(Intangible):
    educationRequirements: EducationalOccupationalCredential | Text | None = None
    estimatedSalary: MonetaryAmount | MonetaryAmountDistribution | Number | None = None
    experienceRequirements: OccupationalExperienceRequirements | Text | None = None
    occupationLocation: AdministrativeArea | None = None
    occupationalCategory: CategoryCode | Text | None = None
    qualifications: EducationalOccupationalCredential | Text | None = None
    responsibilities: Text | None = None
    skills: DefinedTerm | Text | None = None


@dataclass
class HowTo(CreativeWork):
    estimatedCost: MonetaryAmount | Text | None = None
    performTime: Duration | None = None
    prepTime: Duration | None = None
    step: CreativeWork | HowToSection | HowToStep | Text | None = None
    steps: CreativeWork | ItemList | Text | None = None
    supply: HowToSupply | Text | None = None
    tool: HowToTool | Text | None = None
    totalTime: Duration | None = None
    yield_: QuantitativeValue | Text | None = None


@dataclass
class Recipe(HowTo):
    cookTime: Duration | None = None
    cookingMethod: Text | None = None
    ingredients: Text | None = None
    nutrition: NutritionInformation | None = None
    recipeCategory: Text | None = None
    recipeCuisine: Text | None = None
    recipeIngredient: Text | None = None
    recipeInstructions: CreativeWork | ItemList | Text | None = None
    recipeYield: QuantitativeValue | Text | None = None
    suitableForDiet: RestrictedDiet | None = None


@dataclass
class ActionAccessSpecification(Intangible):
    availabilityEnds: Date | DateTime | Time | None = None
    availabilityStarts: Date | DateTime | Time | None = None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None = None
    eligibleRegion: GeoShape | Place | Text | None = None
    expectsAcceptanceOf: Offer | None = None
    ineligibleRegion: GeoShape | Place | Text | None = None
    requiresSubscription: Boolean | MediaSubscription | None = None


@dataclass
class ConsumeAction(Action):
    actionAccessibilityRequirement: ActionAccessSpecification | None = None
    expectsAcceptanceOf: Offer | None = None


@dataclass
class PlayGameAction(ConsumeAction):
    gameAvailabilityType: GameAvailabilityEnumeration | Text | None = None


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
    ownershipFundingInfo: AboutPage | CreativeWork | Text | URL | None = None
    unnamedSourcesPolicy: CreativeWork | URL | None = None
    verificationFactCheckingPolicy: CreativeWork | URL | None = None


@dataclass
class Ticket(Intangible):
    dateIssued: Date | DateTime | None = None
    issuedBy: Organization | None = None
    priceCurrency: Text | None = None
    ticketNumber: Text | None = None
    ticketToken: Text | URL | None = None
    ticketedSeat: Seat | None = None
    totalPrice: Number | PriceSpecification | Text | None = None
    underName: Organization | Person | None = None


@dataclass
class Message(CreativeWork):
    bccRecipient: ContactPoint | Organization | Person | None = None
    ccRecipient: ContactPoint | Organization | Person | None = None
    dateRead: Date | DateTime | None = None
    dateReceived: DateTime | None = None
    dateSent: DateTime | None = None
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
    areaServed: AdministrativeArea | GeoShape | Place | Text | None = None
    availability: ItemAvailability | None = None
    availabilityEnds: Date | DateTime | Time | None = None
    availabilityStarts: Date | DateTime | Time | None = None
    availableAtOrFrom: Place | None = None
    availableDeliveryMethod: DeliveryMethod | None = None
    businessFunction: BusinessFunction | None = None
    deliveryLeadTime: QuantitativeValue | None = None
    eligibleCustomerType: BusinessEntityType | None = None
    eligibleDuration: QuantitativeValue | None = None
    eligibleQuantity: QuantitativeValue | None = None
    eligibleRegion: GeoShape | Place | Text | None = None
    eligibleTransactionVolume: PriceSpecification | None = None
    gtin: Text | None = None
    gtin12: Text | None = None
    gtin13: Text | None = None
    gtin14: Text | None = None
    gtin8: Text | None = None
    includesObject: TypeAndQuantityNode | None = None
    ineligibleRegion: GeoShape | Place | Text | None = None
    inventoryLevel: QuantitativeValue | None = None
    itemCondition: OfferItemCondition | None = None
    itemOffered: AggregateOffer | CreativeWork | Event | MenuItem | Product | Service | Trip | None = None
    mpn: Text | None = None
    priceSpecification: PriceSpecification | None = None
    seller: Organization | Person | None = None
    serialNumber: Text | None = None
    sku: Text | None = None
    validFrom: Date | DateTime | None = None
    validThrough: Date | DateTime | None = None
    warranty: WarrantyPromise | None = None


@dataclass
class Schedule(Intangible):
    byDay: DayOfWeek | Text | None = None
    byMonth: Integer | None = None
    byMonthDay: Integer | None = None
    byMonthWeek: Integer | None = None
    duration: Duration | None = None
    endDate: Date | DateTime | None = None
    endTime: DateTime | Time | None = None
    exceptDate: Date | DateTime | None = None
    repeatCount: Integer | None = None
    repeatFrequency: Duration | Text | None = None
    scheduleTimezone: Text | None = None
    startDate: Date | DateTime | None = None
    startTime: DateTime | Time | None = None


@dataclass
class MedicalGuideline(MedicalEntity):
    evidenceLevel: MedicalEvidenceLevel | None = None
    evidenceOrigin: Text | None = None
    guidelineDate: Date | None = None
    guidelineSubject: MedicalEntity | None = None


@dataclass
class MedicalGuidelineContraindication(MedicalGuideline):
    pass


@dataclass
class MedicalGuidelineRecommendation(MedicalGuideline):
    recommendationStrength: Text | None = None


@dataclass
class Airline(Organization):
    boardingPolicy: BoardingPolicyType | None = None
    iataCode: Text | None = None


@dataclass
class MathSolver(CreativeWork):
    mathExpression: SolveMathAction | Text | None = None


@dataclass
class MusicComposition(CreativeWork):
    composer: Organization | Person | None = None
    firstPerformance: Event | None = None
    includedComposition: MusicComposition | None = None
    iswcCode: Text | None = None
    lyricist: Person | None = None
    lyrics: CreativeWork | None = None
    musicArrangement: MusicComposition | None = None
    musicCompositionForm: Text | None = None
    musicalKey: Text | None = None
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
    alignmentType: Text | None = None
    educationalFramework: Text | None = None
    targetDescription: Text | None = None
    targetName: Text | None = None
    targetUrl: URL | None = None


@dataclass
class Drawing(CreativeWork):
    pass


@dataclass
class Order(Intangible):
    acceptedOffer: Offer | None = None
    billingAddress: PostalAddress | None = None
    broker: Organization | Person | None = None
    confirmationNumber: Text | None = None
    customer: Organization | Person | None = None
    discount: Number | Text | None = None
    discountCode: Text | None = None
    discountCurrency: Text | None = None
    isGift: Boolean | None = None
    merchant: Organization | Person | None = None
    orderDate: Date | DateTime | None = None
    orderDelivery: ParcelDelivery | None = None
    orderNumber: Text | None = None
    orderStatus: OrderStatus | None = None
    orderedItem: OrderItem | Product | Service | None = None
    partOfInvoice: Invoice | None = None
    paymentDue: DateTime | None = None
    paymentDueDate: Date | DateTime | None = None
    paymentMethod: PaymentMethod | None = None
    paymentMethodId: Text | None = None
    paymentUrl: URL | None = None
    seller: Organization | Person | None = None


@dataclass
class OrderItem(Intangible):
    orderDelivery: ParcelDelivery | None = None
    orderItemNumber: Text | None = None
    orderItemStatus: OrderStatus | None = None
    orderQuantity: Number | None = None
    orderedItem: OrderItem | Product | Service | None = None


@dataclass
class MedicalDevice(MedicalEntity):
    adverseOutcome: MedicalEntity | None = None
    contraindication: MedicalContraindication | Text | None = None
    postOp: Text | None = None
    preOp: Text | None = None
    procedure: Text | None = None
    seriousAdverseOutcome: MedicalEntity | None = None


@dataclass
class AnatomicalStructure(MedicalEntity):
    associatedPathophysiology: Text | None = None
    bodyLocation: Text | None = None
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
    muscleAction: Text | None = None
    nerve: Nerve | None = None


@dataclass
class Vessel(AnatomicalStructure):
    pass


@dataclass
class Joint(AnatomicalStructure):
    biomechnicalClass: Text | None = None
    functionalClass: MedicalEntity | Text | None = None
    structuralClass: Text | None = None


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
    negativeNotes: ItemList | ListItem | Text | WebContent | None = None
    positiveNotes: ItemList | ListItem | Text | WebContent | None = None
    reviewAspect: Text | None = None
    reviewBody: Text | None = None
    reviewRating: Rating | None = None


@dataclass
class MediaReview(Review):
    mediaAuthenticityCategory: MediaManipulationRatingEnumeration | None = None
    originalMediaContextDescription: Text | None = None
    originalMediaLink: MediaObject | URL | WebPage | None = None


@dataclass
class Recommendation(Review):
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None = None


@dataclass
class CriticReview(Review):
    pass


@dataclass
class ClaimReview(Review):
    claimReviewed: Text | None = None


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
    membershipNumber: Text | None = None
    membershipPointsEarned: Number | QuantitativeValue | None = None
    programName: Text | None = None


@dataclass
class ServiceChannel(Intangible):
    availableLanguage: Language | Text | None = None
    processingTime: Duration | None = None
    providesService: Service | None = None
    serviceLocation: Place | None = None
    servicePhone: ContactPoint | None = None
    servicePostalAddress: PostalAddress | None = None
    serviceSmsNumber: ContactPoint | None = None
    serviceUrl: URL | None = None


@dataclass
class Role(Intangible):
    endDate: Date | DateTime | None = None
    namedPosition: Text | URL | None = None
    roleName: Text | URL | None = None
    startDate: Date | DateTime | None = None


@dataclass
class PerformanceRole(Role):
    characterName: Text | None = None


@dataclass
class OrganizationRole(Role):
    numberedPosition: Number | None = None


@dataclass
class LinkRole(Role):
    inLanguage: Language | Text | None = None
    linkRelationship: Text | None = None


@dataclass
class NGO(Organization):
    pass


@dataclass
class Clip(CreativeWork):
    actor: Person | None = None
    actors: Person | None = None
    clipNumber: Integer | Text | None = None
    director: Person | None = None
    directors: Person | None = None
    endOffset: HyperTocEntry | Number | None = None
    musicBy: MusicGroup | Person | None = None
    partOfEpisode: Episode | None = None
    partOfSeason: CreativeWorkSeason | None = None
    partOfSeries: CreativeWorkSeries | None = None
    startOffset: HyperTocEntry | Number | None = None


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
    startOffset: HyperTocEntry | Number | None = None


@dataclass
class MedicalCause(MedicalEntity):
    causeOf: MedicalEntity | None = None


@dataclass
class DrugCost(MedicalEntity):
    applicableLocation: AdministrativeArea | None = None
    costCategory: DrugCostCategory | None = None
    costCurrency: Text | None = None
    costOrigin: Text | None = None
    costPerUnit: Number | QualitativeValue | Text | None = None
    drugUnit: Text | None = None


@dataclass
class MusicPlaylist(CreativeWork):
    numTracks: Integer | None = None
    track: ItemList | MusicRecording | None = None
    tracks: MusicRecording | None = None


@dataclass
class MusicRelease(MusicPlaylist):
    catalogNumber: Text | None = None
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
    availableLanguage: Language | Text | None = None
    touristType: Audience | Text | None = None


@dataclass
class TouristDestination(Place):
    includesAttraction: TouristAttraction | None = None
    touristType: Audience | Text | None = None


@dataclass
class PropertyValueSpecification(Intangible):
    defaultValue: Text | Thing | None = None
    maxValue: Number | None = None
    minValue: Number | None = None
    multipleValues: Boolean | None = None
    readonlyValue: Boolean | None = None
    stepValue: Number | None = None
    valueMaxLength: Number | None = None
    valueMinLength: Number | None = None
    valueName: Text | None = None
    valuePattern: Text | None = None
    valueRequired: Boolean | None = None


@dataclass
class Service(Intangible):
    aggregateRating: AggregateRating | None = None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None = None
    audience: Audience | None = None
    availableChannel: ServiceChannel | None = None
    award: Text | None = None
    brand: Brand | Organization | None = None
    broker: Organization | Person | None = None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None = None
    hasOfferCatalog: OfferCatalog | None = None
    hoursAvailable: OpeningHoursSpecification | None = None
    isRelatedTo: Product | Service | None = None
    isSimilarTo: Product | Service | None = None
    logo: ImageObject | URL | None = None
    offers: Demand | Offer | None = None
    produces: Thing | None = None
    provider: Organization | Person | None = None
    providerMobility: Text | None = None
    review: Review | None = None
    serviceArea: AdministrativeArea | GeoShape | Place | None = None
    serviceAudience: Audience | None = None
    serviceOutput: Thing | None = None
    serviceType: GovernmentBenefitsType | Text | None = None
    slogan: Text | None = None
    termsOfService: Text | URL | None = None


@dataclass
class FinancialProduct(Service):
    annualPercentageRate: Number | QuantitativeValue | None = None
    feesAndCommissionsSpecification: Text | URL | None = None
    interestRate: Number | QuantitativeValue | None = None


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
    broadcastDisplayName: Text | None = None
    broadcastFrequency: BroadcastFrequencySpecification | Text | None = None
    broadcastTimezone: Text | None = None
    broadcaster: Organization | None = None
    callSign: Text | None = None
    hasBroadcastChannel: BroadcastChannel | None = None
    inLanguage: Language | Text | None = None
    parentService: BroadcastService | None = None
    videoFormat: Text | None = None


@dataclass
class WebAPI(Service):
    documentation: CreativeWork | URL | None = None


@dataclass
class GovernmentService(Service):
    jurisdiction: AdministrativeArea | Text | None = None
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
    accessCode: Text | None = None
    availableFrom: DateTime | None = None
    availableThrough: DateTime | None = None
    hasDeliveryMethod: DeliveryMethod | None = None


@dataclass
class CreativeWorkSeason(CreativeWork):
    actor: Person | None = None
    director: Person | None = None
    endDate: Date | DateTime | None = None
    episode: Episode | None = None
    episodes: Episode | None = None
    numberOfEpisodes: Integer | None = None
    partOfSeries: CreativeWorkSeries | None = None
    productionCompany: Organization | None = None
    seasonNumber: Integer | Text | None = None
    startDate: Date | DateTime | None = None
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
    healthPlanCostSharing: Boolean | None = None
    healthPlanDrugTier: Text | None = None
    offersPrescriptionByMail: Boolean | None = None


@dataclass
class Legislation(CreativeWork):
    jurisdiction: AdministrativeArea | Text | None = None
    legislationApplies: Legislation | None = None
    legislationChanges: Legislation | None = None
    legislationConsolidates: Legislation | None = None
    legislationDate: Date | None = None
    legislationDateVersion: Date | None = None
    legislationIdentifier: Text | URL | None = None
    legislationJurisdiction: AdministrativeArea | Text | None = None
    legislationLegalForce: LegalForceStatus | None = None
    legislationPassedBy: Organization | Person | None = None
    legislationResponsible: Organization | Person | None = None
    legislationTransposes: Legislation | None = None
    legislationType: CategoryCode | Text | None = None


@dataclass
class LegislationObject(Legislation, MediaObject):
    legislationLegalValue: LegalValueLevel | None = None


@dataclass
class DataFeedItem(Intangible):
    dateCreated: Date | DateTime | None = None
    dateDeleted: Date | DateTime | None = None
    dateModified: Date | DateTime | None = None
    item: Thing | None = None


@dataclass
class Corporation(Organization):
    tickerSymbol: Text | None = None


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
    episodeNumber: Integer | Text | None = None
    musicBy: MusicGroup | Person | None = None
    partOfSeason: CreativeWorkSeason | None = None
    partOfSeries: CreativeWorkSeries | None = None
    productionCompany: Organization | None = None
    trailer: VideoObject | None = None


@dataclass
class TVEpisode(Episode):
    countryOfOrigin: Country | None = None
    partOfTVSeries: TVSeries | None = None
    subtitleLanguage: Language | Text | None = None
    titleEIDR: Text | URL | None = None


@dataclass
class RadioEpisode(Episode):
    pass


@dataclass
class PodcastEpisode(Episode):
    pass


@dataclass
class VisualArtwork(CreativeWork):
    artEdition: Integer | Text | None = None
    artMedium: Text | URL | None = None
    artform: Text | URL | None = None
    artist: Person | None = None
    artworkSurface: Text | URL | None = None
    colorist: Person | None = None
    depth: Distance | QuantitativeValue | None = None
    height: Distance | QuantitativeValue | None = None
    inker: Person | None = None
    letterer: Person | None = None
    penciler: Person | None = None
    surface: Text | URL | None = None
    width: Distance | QuantitativeValue | None = None


@dataclass
class CoverArt(VisualArtwork):
    pass


@dataclass
class ItemList(Intangible):
    itemListElement: ListItem | Text | Thing | None = None
    itemListOrder: ItemListOrderType | Text | None = None
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
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None = None
    datePosted: Date | DateTime | None = None
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
    productGroupID: Text | None = None
    variesBy: DefinedTerm | Text | None = None


@dataclass
class FloorPlan(Intangible):
    amenityFeature: LocationFeatureSpecification | None = None
    floorSize: QuantitativeValue | None = None
    isPlanForApartment: Accommodation | None = None
    layoutImage: ImageObject | URL | None = None
    numberOfAccommodationUnits: QuantitativeValue | None = None
    numberOfAvailableAccommodationUnits: QuantitativeValue | None = None
    numberOfBathroomsTotal: Integer | None = None
    numberOfBedrooms: Number | QuantitativeValue | None = None
    numberOfFullBathrooms: Number | None = None
    numberOfPartialBathrooms: Number | None = None
    numberOfRooms: Number | QuantitativeValue | None = None
    petsAllowed: Boolean | Text | None = None


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
    subtitleLanguage: Language | Text | None = None
    titleEIDR: Text | URL | None = None
    trailer: VideoObject | None = None


@dataclass
class HealthInsurancePlan(Intangible):
    benefitsSummaryUrl: URL | None = None
    contactPoint: ContactPoint | None = None
    healthPlanDrugOption: Text | None = None
    healthPlanDrugTier: Text | None = None
    healthPlanId: Text | None = None
    healthPlanMarketingUrl: URL | None = None
    includesHealthPlanFormulary: HealthPlanFormulary | None = None
    includesHealthPlanNetwork: HealthPlanNetwork | None = None
    usesHealthPlanIdStandard: Text | URL | None = None


@dataclass
class Trip(Intangible):
    arrivalTime: DateTime | Time | None = None
    departureTime: DateTime | Time | None = None
    itinerary: ItemList | Place | None = None
    offers: Demand | Offer | None = None
    partOfTrip: Trip | None = None
    provider: Organization | Person | None = None
    subTrip: Trip | None = None


@dataclass
class Flight(Trip):
    aircraft: Text | Vehicle | None = None
    arrivalAirport: Airport | None = None
    arrivalGate: Text | None = None
    arrivalTerminal: Text | None = None
    boardingPolicy: BoardingPolicyType | None = None
    carrier: Organization | None = None
    departureAirport: Airport | None = None
    departureGate: Text | None = None
    departureTerminal: Text | None = None
    estimatedFlightDuration: Duration | Text | None = None
    flightDistance: Distance | Text | None = None
    flightNumber: Text | None = None
    mealService: Text | None = None
    seller: Organization | Person | None = None
    webCheckinTime: DateTime | None = None


@dataclass
class TrainTrip(Trip):
    arrivalPlatform: Text | None = None
    arrivalStation: TrainStation | None = None
    departurePlatform: Text | None = None
    departureStation: TrainStation | None = None
    trainName: Text | None = None
    trainNumber: Text | None = None


@dataclass
class TouristTrip(Trip):
    touristType: Audience | Text | None = None


@dataclass
class BoatTrip(Trip):
    arrivalBoatTerminal: BoatTerminal | None = None
    departureBoatTerminal: BoatTerminal | None = None


@dataclass
class BusTrip(Trip):
    arrivalBusStop: BusStation | BusStop | None = None
    busName: Text | None = None
    busNumber: Text | None = None
    departureBusStop: BusStation | BusStop | None = None


@dataclass
class Painting(CreativeWork):
    pass


@dataclass
class MedicalCondition(MedicalEntity):
    associatedAnatomy: AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy | None = None
    differentialDiagnosis: DDxElement | None = None
    drug: Drug | None = None
    epidemiology: Text | None = None
    expectedPrognosis: Text | None = None
    naturalProgression: Text | None = None
    pathophysiology: Text | None = None
    possibleComplication: Text | None = None
    possibleTreatment: MedicalTherapy | None = None
    primaryPrevention: MedicalTherapy | None = None
    riskFactor: MedicalRiskFactor | None = None
    secondaryPrevention: MedicalTherapy | None = None
    signOrSymptom: MedicalSignOrSymptom | None = None
    stage: MedicalConditionStage | None = None
    status: EventStatusType | MedicalStudyStatus | Text | None = None
    typicalTest: MedicalTest | None = None


@dataclass
class InfectiousDisease(MedicalCondition):
    infectiousAgent: Text | None = None
    infectiousAgentClass: InfectiousAgentClass | None = None
    transmissionMethod: Text | None = None


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
    inLanguage: Language | Text | None = None
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
    status: EventStatusType | MedicalStudyStatus | Text | None = None
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
    termCode: Text | None = None


@dataclass
class CategoryCode(DefinedTerm):
    codeValue: Text | None = None
    inCodeSet: CategoryCodeSet | URL | None = None


@dataclass
class HyperTocEntry(CreativeWork):
    associatedMedia: MediaObject | None = None
    tocContinuation: HyperTocEntry | None = None
    utterances: Text | None = None


@dataclass
class MedicalRiskFactor(MedicalEntity):
    increasesRiskOf: MedicalEntity | None = None


@dataclass
class MedicalTest(MedicalEntity):
    affectedBy: Drug | None = None
    normalRange: MedicalEnumeration | Text | None = None
    signDetected: MedicalSign | None = None
    usedToDiagnose: MedicalCondition | None = None
    usesDevice: MedicalDevice | None = None


@dataclass
class PathologyTest(MedicalTest):
    tissueSample: Text | None = None


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
    gameEdition: Text | None = None
    gamePlatform: Text | Thing | URL | None = None
    gameServer: GameServer | None = None
    gameTip: CreativeWork | None = None
    musicBy: MusicGroup | Person | None = None
    playMode: GamePlayMode | None = None
    trailer: VideoObject | None = None


@dataclass
class EntryPoint(Intangible):
    actionApplication: SoftwareApplication | None = None
    actionPlatform: DigitalPlatformEnumeration | Text | URL | None = None
    application: SoftwareApplication | None = None
    contentType: Text | None = None
    encodingType: Text | None = None
    httpMethod: Text | None = None
    urlTemplate: Text | None = None


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
    broadcastChannelId: Text | None = None
    broadcastFrequency: BroadcastFrequencySpecification | Text | None = None
    broadcastServiceTier: Text | None = None
    genre: Text | URL | None = None
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
    openingHours: Text | None = None


@dataclass
class RVPark(CivicStructure):
    pass


@dataclass
class Airport(CivicStructure):
    iataCode: Text | None = None
    icaoCode: Text | None = None


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
    query: Text | None = None


@dataclass
class BedDetails(Intangible):
    numberOfBeds: Number | None = None
    typeOfBed: BedType | Text | None = None


@dataclass
class ListItem(Intangible):
    item: Thing | None = None
    nextItem: ListItem | None = None
    position: Integer | Text | None = None
    previousItem: ListItem | None = None


@dataclass
class HowToDirection(CreativeWork, ListItem):
    afterMedia: MediaObject | URL | None = None
    beforeMedia: MediaObject | URL | None = None
    duringMedia: MediaObject | URL | None = None
    performTime: Duration | None = None
    prepTime: Duration | None = None
    supply: HowToSupply | Text | None = None
    tool: HowToTool | Text | None = None
    totalTime: Duration | None = None


@dataclass
class HowToItem(ListItem):
    requiredQuantity: Number | QuantitativeValue | Text | None = None


@dataclass
class HowToSection(CreativeWork, ItemList, ListItem):
    steps: CreativeWork | ItemList | Text | None = None


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
    issn: Text | None = None


@dataclass
class Quotation(CreativeWork):
    spokenByCharacter: Organization | Person | None = None


@dataclass
class Article(CreativeWork):
    articleBody: Text | None = None
    articleSection: Text | None = None
    backstory: CreativeWork | Text | None = None
    pageEnd: Integer | Text | None = None
    pageStart: Integer | Text | None = None
    pagination: Text | None = None
    speakable: SpeakableSpecification | URL | None = None
    wordCount: Integer | None = None


@dataclass
class NewsArticle(Article):
    dateline: Text | None = None
    printColumn: Text | None = None
    printEdition: Text | None = None
    printPage: Text | None = None
    printSection: Text | None = None


@dataclass
class SocialMediaPosting(Article):
    sharedContent: CreativeWork | None = None


@dataclass
class Report(Article):
    reportNumber: Text | None = None


@dataclass
class TechArticle(Article):
    dependencies: Text | None = None
    proficiencyLevel: Text | None = None


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
    pageEnd: Integer | Text | None = None
    pageStart: Integer | Text | None = None
    pagination: Text | None = None


@dataclass
class PublicationIssue(CreativeWork):
    issueNumber: Integer | Text | None = None
    pageEnd: Integer | Text | None = None
    pageStart: Integer | Text | None = None
    pagination: Text | None = None


@dataclass
class ComicIssue(PublicationIssue):
    artist: Person | None = None
    colorist: Person | None = None
    inker: Person | None = None
    letterer: Person | None = None
    penciler: Person | None = None
    variantCover: Text | None = None


@dataclass
class PublicationVolume(CreativeWork):
    pageEnd: Integer | Text | None = None
    pageStart: Integer | Text | None = None
    pagination: Text | None = None
    volumeNumber: Integer | Text | None = None


@dataclass
class Observation(Intangible):
    marginOfError: QuantitativeValue | None = None
    measuredProperty: Property | None = None
    measuredValue: DataType | None = None
    observationDate: DateTime | None = None
    observedNode: StatisticalPopulation | None = None


@dataclass
class MedicalRiskEstimator(MedicalEntity):
    estimatesRiskOf: MedicalEntity | None = None
    includedRiskFactor: MedicalRiskFactor | None = None


@dataclass
class MedicalRiskScore(MedicalRiskEstimator):
    algorithm: Text | None = None


@dataclass
class MedicalRiskCalculator(MedicalRiskEstimator):
    pass


@dataclass
class ScreeningEvent(Event):
    subtitleLanguage: Language | Text | None = None
    videoFormat: Text | None = None
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
    seatNumber: Text | None = None
    seatRow: Text | None = None
    seatSection: Text | None = None
    seatingType: QualitativeValue | Text | None = None


@dataclass
class Audience(Intangible):
    audienceType: Text | None = None
    geographicArea: AdministrativeArea | None = None


@dataclass
class PeopleAudience(Audience):
    healthCondition: MedicalCondition | None = None
    requiredGender: Text | None = None
    requiredMaxAge: Integer | None = None
    requiredMinAge: Integer | None = None
    suggestedAge: QuantitativeValue | None = None
    suggestedGender: GenderType | Text | None = None
    suggestedMaxAge: Number | None = None
    suggestedMeasurement: QuantitativeValue | None = None
    suggestedMinAge: Number | None = None


@dataclass
class BusinessAudience(Audience):
    numberOfEmployees: QuantitativeValue | None = None
    yearlyRevenue: QuantitativeValue | None = None
    yearsInOperation: QuantitativeValue | None = None


@dataclass
class EducationalAudience(Audience):
    educationalRole: Text | None = None


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
    hasBioPolymerSequence: Text | None = None


@dataclass
class BroadcastFrequencySpecification(Intangible):
    broadcastFrequencyValue: Number | QuantitativeValue | None = None
    broadcastSignalModulation: QualitativeValue | Text | None = None
    broadcastSubChannel: Text | None = None


@dataclass
class SolveMathAction(Action):
    eduQuestionType: Text | None = None


@dataclass
class IndividualProduct(Product):
    serialNumber: Text | None = None


@dataclass
class AnatomicalSystem(MedicalEntity):
    associatedPathophysiology: Text | None = None
    comprisedOf: AnatomicalStructure | AnatomicalSystem | None = None
    relatedCondition: MedicalCondition | None = None
    relatedStructure: AnatomicalStructure | None = None
    relatedTherapy: MedicalTherapy | None = None


@dataclass
class SuperficialAnatomy(MedicalEntity):
    associatedPathophysiology: Text | None = None
    relatedAnatomy: AnatomicalStructure | AnatomicalSystem | None = None
    relatedCondition: MedicalCondition | None = None
    relatedTherapy: MedicalTherapy | None = None
    significance: Text | None = None


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
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | Text | None = None


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
    amount: MonetaryAmount | Number | None = None
    funder: Organization | Person | None = None


@dataclass
class Substance(MedicalEntity):
    activeIngredient: Text | None = None
    maximumIntake: MaximumDoseSchedule | None = None


@dataclass
class DietarySupplement(Substance):
    activeIngredient: Text | None = None
    isProprietary: Boolean | None = None
    legalStatus: DrugLegalStatus | MedicalEnumeration | Text | None = None
    manufacturer: Organization | None = None
    maximumIntake: MaximumDoseSchedule | None = None
    mechanismOfAction: Text | None = None
    nonProprietaryName: Text | None = None
    proprietaryName: Text | None = None
    recommendedIntake: RecommendedDoseSchedule | None = None
    safetyConsideration: Text | None = None
    targetPopulation: Text | None = None


@dataclass
class Drug(Substance):
    activeIngredient: Text | None = None
    administrationRoute: Text | None = None
    alcoholWarning: Text | None = None
    availableStrength: DrugStrength | None = None
    breastfeedingWarning: Text | None = None
    clincalPharmacology: Text | None = None
    clinicalPharmacology: Text | None = None
    dosageForm: Text | None = None
    doseSchedule: DoseSchedule | None = None
    drugClass: DrugClass | None = None
    drugUnit: Text | None = None
    foodWarning: Text | None = None
    includedInHealthInsurancePlan: HealthInsurancePlan | None = None
    interactingDrug: Drug | None = None
    isAvailableGenerically: Boolean | None = None
    isProprietary: Boolean | None = None
    labelDetails: URL | None = None
    legalStatus: DrugLegalStatus | MedicalEnumeration | Text | None = None
    manufacturer: Organization | None = None
    maximumIntake: MaximumDoseSchedule | None = None
    mechanismOfAction: Text | None = None
    nonProprietaryName: Text | None = None
    overdosage: Text | None = None
    pregnancyCategory: DrugPregnancyCategory | None = None
    pregnancyWarning: Text | None = None
    prescribingInfo: URL | None = None
    prescriptionStatus: DrugPrescriptionStatus | Text | None = None
    proprietaryName: Text | None = None
    relatedDrug: Drug | None = None
    rxcui: Text | None = None
    warning: Text | URL | None = None


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
    free: Boolean | None = None
    publishedBy: Organization | Person | None = None
    publishedOn: BroadcastService | None = None


@dataclass
class BroadcastEvent(PublicationEvent):
    broadcastOfEvent: Event | None = None
    isLiveBroadcast: Boolean | None = None
    subtitleLanguage: Language | Text | None = None
    videoFormat: Text | None = None


@dataclass
class OnDemandEvent(PublicationEvent):
    pass


@dataclass
class Blog(CreativeWork):
    blogPost: BlogPosting | None = None
    blogPosts: BlogPosting | None = None
    issn: Text | None = None


@dataclass
class Guide(CreativeWork):
    reviewAspect: Text | None = None


@dataclass
class Rating(Intangible):
    author: Organization | Person | None = None
    bestRating: Number | Text | None = None
    ratingExplanation: Text | None = None
    ratingValue: Number | Text | None = None
    reviewAspect: Text | None = None
    worstRating: Number | Text | None = None


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
    scheduledTime: DateTime | None = None


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
    inChI: Text | None = None
    inChIKey: Text | None = None
    iupacName: Text | None = None
    molecularFormula: Text | None = None
    molecularWeight: QuantitativeValue | Text | None = None
    monoisotopicMolecularWeight: QuantitativeValue | Text | None = None
    potentialUse: DefinedTerm | None = None
    smiles: Text | None = None


@dataclass
class CourseInstance(Event):
    courseMode: Text | URL | None = None
    courseWorkload: Text | None = None
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
    eduQuestionType: Text | None = None
    suggestedAnswer: Answer | ItemList | None = None


@dataclass
class Play(CreativeWork):
    pass


@dataclass
class ArchiveComponent(CreativeWork):
    holdingArchive: ArchiveOrganization | None = None
    itemLocation: Place | PostalAddress | Text | None = None


@dataclass
class DataCatalog(CreativeWork):
    dataset: Dataset | None = None
    measurementTechnique: Text | URL | None = None


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
    hasBioPolymerSequence: Text | None = None


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
    cvdCollectionDate: DateTime | Text | None = None
    cvdFacilityCounty: Text | None = None
    cvdFacilityId: Text | None = None
    cvdNumBeds: Number | None = None
    cvdNumBedsOcc: Number | None = None
    cvdNumC19Died: Number | None = None
    cvdNumC19HOPats: Number | None = None
    cvdNumC19HospPats: Number | None = None
    cvdNumC19MechVentPats: Number | None = None
    cvdNumC19OFMechVentPats: Number | None = None
    cvdNumC19OverflowPats: Number | None = None
    cvdNumICUBeds: Number | None = None
    cvdNumICUBedsOcc: Number | None = None
    cvdNumTotBeds: Number | None = None
    cvdNumVent: Number | None = None
    cvdNumVentUse: Number | None = None
    datePosted: Date | DateTime | None = None


@dataclass
class PriceSpecification(StructuredValue):
    eligibleQuantity: QuantitativeValue | None = None
    eligibleTransactionVolume: PriceSpecification | None = None
    maxPrice: Number | None = None
    minPrice: Number | None = None
    price: Number | Text | None = None
    priceCurrency: Text | None = None
    validFrom: Date | DateTime | None = None
    validThrough: Date | DateTime | None = None
    valueAddedTaxIncluded: Boolean | None = None


@dataclass
class ShippingDeliveryTime(StructuredValue):
    businessDays: OpeningHoursSpecification | None = None
    cutoffTime: Time | None = None
    handlingTime: QuantitativeValue | None = None
    transitTime: QuantitativeValue | None = None


@dataclass
class QuantitativeValueDistribution(StructuredValue):
    duration: Duration | None = None
    median: Number | None = None
    percentile10: Number | None = None
    percentile25: Number | None = None
    percentile75: Number | None = None
    percentile90: Number | None = None


@dataclass
class DeliveryTimeSettings(StructuredValue):
    deliveryTime: ShippingDeliveryTime | None = None
    isUnlabelledFallback: Boolean | None = None
    shippingDestination: DefinedRegion | None = None
    transitTimeLabel: Text | None = None


@dataclass
class OfferShippingDetails(StructuredValue):
    deliveryTime: ShippingDeliveryTime | None = None
    doesNotShip: Boolean | None = None
    shippingDestination: DefinedRegion | None = None
    shippingLabel: Text | None = None
    shippingRate: MonetaryAmount | None = None
    shippingSettingsLink: URL | None = None
    transitTimeLabel: Text | None = None


@dataclass
class ShippingRateSettings(StructuredValue):
    doesNotShip: Boolean | None = None
    freeShippingThreshold: DeliveryChargeSpecification | MonetaryAmount | None = None
    isUnlabelledFallback: Boolean | None = None
    shippingDestination: DefinedRegion | None = None
    shippingLabel: Text | None = None
    shippingRate: MonetaryAmount | None = None


@dataclass
class ContactPoint(StructuredValue):
    areaServed: AdministrativeArea | GeoShape | Place | Text | None = None
    availableLanguage: Language | Text | None = None
    contactOption: ContactPointOption | None = None
    contactType: Text | None = None
    email: Text | None = None
    faxNumber: Text | None = None
    hoursAvailable: OpeningHoursSpecification | None = None
    productSupported: Product | Text | None = None
    serviceArea: AdministrativeArea | GeoShape | Place | None = None
    telephone: Text | None = None


@dataclass
class PropertyValue(StructuredValue):
    maxValue: Number | None = None
    measurementTechnique: Text | URL | None = None
    minValue: Number | None = None
    propertyID: Text | URL | None = None
    unitCode: Text | URL | None = None
    unitText: Text | None = None
    value: Boolean | Number | StructuredValue | Text | None = None
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | Text | None = None


@dataclass
class QuantitativeValue(StructuredValue):
    additionalProperty: PropertyValue | None = None
    maxValue: Number | None = None
    minValue: Number | None = None
    unitCode: Text | URL | None = None
    unitText: Text | None = None
    value: Boolean | Number | StructuredValue | Text | None = None
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | Text | None = None


@dataclass
class DefinedRegion(StructuredValue):
    addressCountry: Country | Text | None = None
    addressRegion: Text | None = None
    postalCode: Text | None = None
    postalCodePrefix: Text | None = None
    postalCodeRange: PostalCodeRangeSpecification | None = None


@dataclass
class GeoCoordinates(StructuredValue):
    address: PostalAddress | Text | None = None
    addressCountry: Country | Text | None = None
    elevation: Number | Text | None = None
    latitude: Number | Text | None = None
    longitude: Number | Text | None = None
    postalCode: Text | None = None


@dataclass
class GeoShape(StructuredValue):
    address: PostalAddress | Text | None = None
    addressCountry: Country | Text | None = None
    box: Text | None = None
    circle: Text | None = None
    elevation: Number | Text | None = None
    line: Text | None = None
    polygon: Text | None = None
    postalCode: Text | None = None


@dataclass
class NutritionInformation(StructuredValue):
    calories: Energy | None = None
    carbohydrateContent: Mass | None = None
    cholesterolContent: Mass | None = None
    fatContent: Mass | None = None
    fiberContent: Mass | None = None
    proteinContent: Mass | None = None
    saturatedFatContent: Mass | None = None
    servingSize: Text | None = None
    sodiumContent: Mass | None = None
    sugarContent: Mass | None = None
    transFatContent: Mass | None = None
    unsaturatedFatContent: Mass | None = None


@dataclass
class OwnershipInfo(StructuredValue):
    acquiredFrom: Organization | Person | None = None
    ownedFrom: DateTime | None = None
    ownedThrough: DateTime | None = None
    typeOfGood: Product | Service | None = None


@dataclass
class DatedMoneySpecification(StructuredValue):
    amount: MonetaryAmount | Number | None = None
    currency: Text | None = None
    endDate: Date | DateTime | None = None
    startDate: Date | DateTime | None = None


@dataclass
class OpeningHoursSpecification(StructuredValue):
    closes: Time | None = None
    dayOfWeek: DayOfWeek | None = None
    opens: Time | None = None
    validFrom: Date | DateTime | None = None
    validThrough: Date | DateTime | None = None


@dataclass
class RepaymentSpecification(StructuredValue):
    downPayment: MonetaryAmount | Number | None = None
    earlyPrepaymentPenalty: MonetaryAmount | None = None
    loanPaymentAmount: MonetaryAmount | None = None
    loanPaymentFrequency: Number | None = None
    numberOfLoanPayments: Number | None = None


@dataclass
class MonetaryAmount(StructuredValue):
    currency: Text | None = None
    maxValue: Number | None = None
    minValue: Number | None = None
    validFrom: Date | DateTime | None = None
    validThrough: Date | DateTime | None = None
    value: Boolean | Number | StructuredValue | Text | None = None


@dataclass
class TypeAndQuantityNode(StructuredValue):
    amountOfThisGood: Number | None = None
    businessFunction: BusinessFunction | None = None
    typeOfGood: Product | Service | None = None
    unitCode: Text | URL | None = None
    unitText: Text | None = None


@dataclass
class InteractionCounter(StructuredValue):
    endTime: DateTime | Time | None = None
    interactionService: SoftwareApplication | WebSite | None = None
    interactionType: Action | None = None
    location: Place | PostalAddress | Text | VirtualLocation | None = None
    startTime: DateTime | Time | None = None
    userInteractionCount: Integer | None = None


@dataclass
class EngineSpecification(StructuredValue):
    engineDisplacement: QuantitativeValue | None = None
    enginePower: QuantitativeValue | None = None
    engineType: QualitativeValue | Text | URL | None = None
    fuelType: QualitativeValue | Text | URL | None = None
    torque: QuantitativeValue | None = None


@dataclass
class ExchangeRateSpecification(StructuredValue):
    currency: Text | None = None
    currentExchangeRate: UnitPriceSpecification | None = None
    exchangeRateSpread: MonetaryAmount | Number | None = None


@dataclass
class PostalCodeRangeSpecification(StructuredValue):
    postalCodeBegin: Text | None = None
    postalCodeEnd: Text | None = None


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
    amount: MonetaryAmount | Number | None = None
    beneficiaryBank: BankOrCreditUnion | Text | None = None


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
    numberOfBedrooms: Number | QuantitativeValue | None = None
    petsAllowed: Boolean | Text | None = None
    tourBookingPage: URL | None = None


@dataclass
class Conversation(CreativeWork):
    pass


@dataclass
class LifestyleModification(MedicalEntity):
    pass


@dataclass
class Diet(CreativeWork, LifestyleModification):
    dietFeatures: Text | None = None
    endorsers: Organization | Person | None = None
    expertConsiderations: Text | None = None
    physiologicalBenefits: Text | None = None
    risks: Text | None = None


@dataclass
class PhysicalActivity(LifestyleModification):
    associatedAnatomy: AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy | None = None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None = None
    epidemiology: Text | None = None
    pathophysiology: Text | None = None


@dataclass
class Atlas(CreativeWork):
    pass


@dataclass
class Season(CreativeWork):
    pass


@dataclass
class SportsOrganization(Organization):
    sport: Text | URL | None = None


@dataclass
class SportsTeam(SportsOrganization):
    athlete: Person | None = None
    coach: Person | None = None
    gender: GenderType | Text | None = None


@dataclass
class Thesis(CreativeWork):
    inSupportOf: Text | None = None


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
    actionOption: Text | Thing | None = None
    option: Text | Thing | None = None


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
    endDate: Date | DateTime | None = None
    issn: Text | None = None
    startDate: Date | DateTime | None = None


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
    price: Number | Text | None = None
    priceCurrency: Text | None = None
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
    monthsOfExperience: Number | None = None


@dataclass
class ChemicalSubstance(BioChemEntity):
    chemicalComposition: Text | None = None
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
    genre: Text | URL | None = None
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
    inLanguage: Language | Text | None = None
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
    doseUnit: Text | None = None
    doseValue: Number | QualitativeValue | None = None
    frequency: Text | None = None
    targetPopulation: Text | None = None


@dataclass
class DrugStrength(MedicalIntangible):
    activeIngredient: Text | None = None
    availableIn: AdministrativeArea | None = None
    maximumIntake: MaximumDoseSchedule | None = None
    strengthUnit: Text | None = None
    strengthValue: Number | None = None


@dataclass
class DrugLegalStatus(MedicalIntangible):
    applicableLocation: AdministrativeArea | None = None


@dataclass
class MedicalCode(CategoryCode, MedicalIntangible):
    codeValue: Text | None = None
    codingSystem: Text | None = None


@dataclass
class MedicalConditionStage(MedicalIntangible):
    stageAsNumber: Number | None = None
    subStageSuffix: Text | None = None


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
    commentText: Text | None = None
    commentTime: Date | DateTime | None = None
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
    currenciesAccepted: Text | None = None
    openingHours: Text | None = None
    paymentAccepted: Text | None = None
    priceRange: Text | None = None


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
    acceptsReservations: Boolean | Text | URL | None = None
    hasMenu: Menu | Text | URL | None = None
    menu: Menu | Text | URL | None = None
    servesCuisine: Text | None = None
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
    availableLanguage: Language | Text | None = None
    checkinTime: DateTime | Time | None = None
    checkoutTime: DateTime | Time | None = None
    numberOfRooms: Number | QuantitativeValue | None = None
    petsAllowed: Boolean | Text | None = None
    starRating: Rating | None = None


@dataclass
class AutomotiveBusiness(LocalBusiness):
    pass


@dataclass
class FinancialService(LocalBusiness):
    feesAndCommissionsSpecification: Text | URL | None = None


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
    bed: BedDetails | BedType | Text | None = None
    occupancy: QuantitativeValue | None = None


@dataclass
class SingleFamilyResidence(House):
    numberOfRooms: Number | QuantitativeValue | None = None
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
    contraindication: MedicalContraindication | Text | None = None
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
    baseSalary: MonetaryAmount | Number | PriceSpecification | None = None
    salaryCurrency: Text | None = None


@dataclass
class InvestmentOrDeposit(FinancialProduct):
    amount: MonetaryAmount | Number | None = None


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
    bankAccountType: Text | URL | None = None


@dataclass
class DepositAccount(BankAccount, InvestmentOrDeposit):
    pass


@dataclass
class LoanOrCredit(FinancialProduct):
    amount: MonetaryAmount | Number | None = None
    currency: Text | None = None
    gracePeriod: Duration | None = None
    loanRepaymentForm: RepaymentSpecification | None = None
    loanTerm: QuantitativeValue | None = None
    loanType: Text | URL | None = None
    recourseLoan: Boolean | None = None
    renegotiableLoan: Boolean | None = None
    requiredCollateral: Text | Thing | None = None


@dataclass
class MortgageLoan(LoanOrCredit):
    domiciledMortgage: Boolean | None = None
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
    additionalNumberOfGuests: Number | None = None
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
    estimatedCost: MonetaryAmount | Text | None = None


@dataclass
class HowToTool(HowToItem):
    pass


@dataclass
class MedicalScholarlyArticle(ScholarlyArticle):
    publicationType: Text | None = None


@dataclass
class APIReference(TechArticle):
    assembly: Text | None = None
    assemblyVersion: Text | None = None
    executableLibraryName: Text | None = None
    programmingModel: Text | None = None
    targetPlatform: Text | None = None


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
    coverageEndTime: DateTime | None = None
    coverageStartTime: DateTime | None = None
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
    childMaxAge: Number | None = None
    childMinAge: Number | None = None


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
    sizeGroup: SizeGroupEnumeration | Text | None = None
    sizeSystem: SizeSystemEnumeration | Text | None = None
    suggestedAge: QuantitativeValue | None = None
    suggestedGender: GenderType | Text | None = None
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
    cashBack: Boolean | Number | None = None
    contactlessPayment: Boolean | None = None
    floorLimit: MonetaryAmount | None = None
    monthlyMinimumRepaymentAmount: MonetaryAmount | Number | None = None


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
    addressCountry: Country | Text | None = None
    addressLocality: Text | None = None
    addressRegion: Text | None = None
    postOfficeBoxNumber: Text | None = None
    postalCode: Text | None = None
    streetAddress: Text | None = None


@dataclass
class CompoundPriceSpecification(PriceSpecification):
    priceComponent: UnitPriceSpecification | None = None
    priceType: PriceTypeEnumeration | Text | None = None


@dataclass
class GeoCircle(GeoShape):
    geoMidpoint: GeoCoordinates | None = None
    geoRadius: Distance | Number | Text | None = None


@dataclass
class UnitPriceSpecification(PriceSpecification):
    billingDuration: Duration | Number | QuantitativeValue | None = None
    billingIncrement: Number | None = None
    billingStart: Number | None = None
    priceComponentType: PriceComponentTypeEnumeration | None = None
    priceType: PriceTypeEnumeration | Text | None = None
    referenceQuantity: QuantitativeValue | None = None
    unitCode: Text | URL | None = None
    unitText: Text | None = None


@dataclass
class LocationFeatureSpecification(PropertyValue):
    hoursAvailable: OpeningHoursSpecification | None = None
    validFrom: Date | DateTime | None = None
    validThrough: Date | DateTime | None = None


@dataclass
class DeliveryChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: DeliveryMethod | None = None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None = None
    eligibleRegion: GeoShape | Place | Text | None = None
    ineligibleRegion: GeoShape | Place | Text | None = None


@dataclass
class PaymentChargeSpecification(PriceSpecification):
    appliesToDeliveryMethod: DeliveryMethod | None = None
    appliesToPaymentMethod: PaymentMethod | None = None


@dataclass
class MonetaryAmountDistribution(QuantitativeValueDistribution):
    currency: Text | None = None


@dataclass
class ExercisePlan(CreativeWork, PhysicalActivity):
    activityDuration: Duration | QuantitativeValue | None = None
    activityFrequency: QuantitativeValue | Text | None = None
    additionalVariable: Text | None = None
    exerciseType: Text | None = None
    intensity: QuantitativeValue | Text | None = None
    repetitions: Number | QuantitativeValue | None = None
    restPeriods: QuantitativeValue | Text | None = None
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
    gamePlatform: Text | Thing | URL | None = None
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
    screenCount: Number | None = None


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
