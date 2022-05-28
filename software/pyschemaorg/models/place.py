# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.593060
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .aggregate_rating import AggregateRating
from .boolean import Boolean
from .defined_term import DefinedTerm
from .event import Event
from .geo_coordinates import GeoCoordinates
from .geo_shape import GeoShape
from .geospatial_geometry import GeospatialGeometry
from .image_object import ImageObject
from .integer import Integer
from .location_feature_specification import LocationFeatureSpecification
from .map import Map
from .number import Number
from .opening_hours_specification import OpeningHoursSpecification
from .photograph import Photograph
from .postal_address import PostalAddress
from .property_value import PropertyValue
from .review import Review
from .text import Text
from .thing import Thing
from .url import URL


@dataclass
class Place(Thing):
    additionalProperty: PropertyValue | None
    address: PostalAddress | Text | None
    aggregateRating: AggregateRating | None
    amenityFeature: LocationFeatureSpecification | None
    branchCode: Text | None
    containedIn: Place | None
    containedInPlace: Place | None
    containsPlace: Place | None
    event: Event | None
    events: Event | None
    faxNumber: Text | None
    geo: GeoCoordinates | GeoShape | None
    geoContains: GeospatialGeometry | Place | None
    geoCoveredBy: GeospatialGeometry | Place | None
    geoCovers: GeospatialGeometry | Place | None
    geoCrosses: GeospatialGeometry | Place | None
    geoDisjoint: GeospatialGeometry | Place | None
    geoEquals: GeospatialGeometry | Place | None
    geoIntersects: GeospatialGeometry | Place | None
    geoOverlaps: GeospatialGeometry | Place | None
    geoTouches: GeospatialGeometry | Place | None
    geoWithin: GeospatialGeometry | Place | None
    globalLocationNumber: Text | None
    hasDriveThroughService: Boolean | None
    hasMap: Map | URL | None
    isAccessibleForFree: Boolean | None
    isicV4: Text | None
    keywords: DefinedTerm | Text | URL | None
    latitude: Number | Text | None
    logo: ImageObject | URL | None
    longitude: Number | Text | None
    map: URL | None
    maps: URL | None
    maximumAttendeeCapacity: Integer | None
    openingHoursSpecification: OpeningHoursSpecification | None
    photo: ImageObject | Photograph | None
    photos: ImageObject | Photograph | None
    publicAccess: Boolean | None
    review: Review | None
    reviews: Review | None
    slogan: Text | None
    smokingAllowed: Boolean | None
    specialOpeningHoursSpecification: OpeningHoursSpecification | None
    telephone: Text | None
    tourBookingPage: URL | None
