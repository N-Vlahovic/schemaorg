# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.616004
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .broadcast_service import BroadcastService
from .event import Event
from .organization import Organization
from .person import Person


@dataclass
class PublicationEvent(Event):
    free: Boolean | None
    publishedBy: Organization | Person | None
    publishedOn: BroadcastService | None
