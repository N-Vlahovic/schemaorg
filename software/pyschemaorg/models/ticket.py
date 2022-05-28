# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578068
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.date_time import DateTime
from models.intangible import Intangible
from models.number import Number
from models.organization import Organization
from models.person import Person
from models.price_specification import PriceSpecification
from models.seat import Seat
from models.text import Text
from models.url import URL


@dataclass
class Ticket(Intangible):
    dateIssued: Date | DateTime | None
    issuedBy: Organization | None
    priceCurrency: Text | None
    ticketNumber: Text | None
    ticketToken: Text | URL | None
    ticketedSeat: Seat | None
    totalPrice: Number | PriceSpecification | Text | None
    underName: Organization | Person | None
