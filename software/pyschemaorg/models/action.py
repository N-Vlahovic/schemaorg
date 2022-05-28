# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582897
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.action_status_type import ActionStatusType
from models.date_time import DateTime
from models.entry_point import EntryPoint
from models.organization import Organization
from models.person import Person
from models.place import Place
from models.postal_address import PostalAddress
from models.text import Text
from models.thing import Thing
from models.time import Time
from models.virtual_location import VirtualLocation


@dataclass
class Action(Thing):
    actionStatus: ActionStatusType | None
    agent: Organization | Person | None
    endTime: DateTime | Time | None
    error: Thing | None
    instrument: Thing | None
    location: Place | PostalAddress | Text | VirtualLocation | None
    object: Thing | None
    participant: Organization | Person | None
    provider: Organization | Person | None
    result: Thing | None
    startTime: DateTime | Time | None
    target: EntryPoint | None
