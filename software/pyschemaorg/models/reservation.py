# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575821
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date_time import DateTime
from models.intangible import Intangible
from models.number import Number
from models.organization import Organization
from models.person import Person
from models.price_specification import PriceSpecification
from models.program_membership import ProgramMembership
from models.reservation_status_type import ReservationStatusType
from models.text import Text
from models.thing import Thing
from models.ticket import Ticket


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
