# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.588817
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date import Date
from .date_time import DateTime
from .intangible import Intangible
from .number import Number
from .organization import Organization
from .person import Person
from .price_specification import PriceSpecification
from .seat import Seat
from .text import Text
from .url import URL


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
