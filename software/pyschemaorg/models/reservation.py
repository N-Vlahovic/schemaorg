# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.584164
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date_time import DateTime
from .intangible import Intangible
from .number import Number
from .organization import Organization
from .person import Person
from .price_specification import PriceSpecification
from .program_membership import ProgramMembership
from .reservation_status_type import ReservationStatusType
from .text import Text
from .thing import Thing
from .ticket import Ticket


@dataclass
class Reservation(Intangible):
    bookingAgent: Organization | Person | None
    bookingTime: DateTime | None
    broker: Organization | Person | None
    modifiedTime: DateTime | None
    priceCurrency: Text | None
    programMembershipUsed: ProgramMembership | None
    provider: Organization | Person | None
    reservationFor: Thing | None
    reservationId: Text | None
    reservationStatus: ReservationStatusType | None
    reservedTicket: Ticket | None
    totalPrice: Number | PriceSpecification | Text | None
    underName: Organization | Person | None
