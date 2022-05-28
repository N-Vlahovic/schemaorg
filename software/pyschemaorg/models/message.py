# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578274
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.audience import Audience
from models.contact_point import ContactPoint
from models.creative_work import CreativeWork
from models.date import Date
from models.date_time import DateTime
from models.organization import Organization
from models.person import Person


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
