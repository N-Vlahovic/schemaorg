# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.590641
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .aggregate_rating import AggregateRating
from .audience import Audience
from .boolean import Boolean
from .creative_work import CreativeWork
from .date import Date
from .date_time import DateTime
from .defined_term import DefinedTerm
from .demand import Demand
from .duration import Duration
from .event_attendance_mode_enumeration import EventAttendanceModeEnumeration
from .event_status_type import EventStatusType
from .grant import Grant
from .integer import Integer
from .language import Language
from .offer import Offer
from .organization import Organization
from .person import Person
from .place import Place
from .postal_address import PostalAddress
from .review import Review
from .schedule import Schedule
from .text import Text
from .thing import Thing
from .time import Time
from .url import URL
from .virtual_location import VirtualLocation


@dataclass
class Event(Thing):
    about: Thing | None
    actor: Person | None
    aggregateRating: AggregateRating | None
    attendee: Organization | Person | None
    attendees: Organization | Person | None
    audience: Audience | None
    composer: Organization | Person | None
    contributor: Organization | Person | None
    director: Person | None
    doorTime: DateTime | Time | None
    duration: Duration | None
    endDate: Date | DateTime | None
    eventAttendanceMode: EventAttendanceModeEnumeration | None
    eventSchedule: Schedule | None
    eventStatus: EventStatusType | None
    funder: Organization | Person | None
    funding: Grant | None
    inLanguage: Language | Text | None
    isAccessibleForFree: Boolean | None
    keywords: DefinedTerm | Text | URL | None
    location: Place | PostalAddress | Text | VirtualLocation | None
    maximumAttendeeCapacity: Integer | None
    maximumPhysicalAttendeeCapacity: Integer | None
    maximumVirtualAttendeeCapacity: Integer | None
    offers: Demand | Offer | None
    organizer: Organization | Person | None
    performer: Organization | Person | None
    performers: Organization | Person | None
    previousStartDate: Date | None
    recordedIn: CreativeWork | None
    remainingAttendeeCapacity: Integer | None
    review: Review | None
    sponsor: Organization | Person | None
    startDate: Date | DateTime | None
    subEvent: Event | None
    subEvents: Event | None
    superEvent: Event | None
    translator: Organization | Person | None
    typicalAgeRange: Text | None
    workFeatured: CreativeWork | None
    workPerformed: CreativeWork | None
