# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.589232
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .audience import Audience
from .contact_point import ContactPoint
from .creative_work import CreativeWork
from .date import Date
from .date_time import DateTime
from .organization import Organization
from .person import Person


@dataclass
class Message(CreativeWork):
    bccRecipient: ContactPoint | Organization | Person | None
    ccRecipient: ContactPoint | Organization | Person | None
    dateRead: Date | DateTime | None
    dateReceived: DateTime | None
    dateSent: DateTime | None
    messageAttachment: CreativeWork | None
    recipient: Audience | ContactPoint | Organization | Person | None
    sender: Audience | Organization | Person | None
    toRecipient: Audience | ContactPoint | Organization | Person | None
