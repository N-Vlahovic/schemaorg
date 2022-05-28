# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594195
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.broadcast_service import BroadcastService
from models.event import Event
from models.organization import Organization
from models.person import Person


@dataclass
class PublicationEvent(Event):
    free: Boolean | None
    publishedBy: Organization | Person | None
    publishedOn: BroadcastService | None
