# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578971
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.aggregate_rating import AggregateRating
from models.audience import Audience
from models.boolean import Boolean
from models.creative_work import CreativeWork
from models.date import Date
from models.date_time import DateTime
from models.defined_term import DefinedTerm
from models.demand import Demand
from models.duration import Duration
from models.event_attendance_mode_enumeration import EventAttendanceModeEnumeration
from models.event_status_type import EventStatusType
from models.grant import Grant
from models.integer import Integer
from models.language import Language
from models.offer import Offer
from models.organization import Organization
from models.person import Person
from models.place import Place
from models.postal_address import PostalAddress
from models.review import Review
from models.schedule import Schedule
from models.text import Text
from models.thing import Thing
from models.time import Time
from models.url import URL
from models.virtual_location import VirtualLocation


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
