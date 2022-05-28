# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.597091
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .action_status_type import ActionStatusType
from .date_time import DateTime
from .entry_point import EntryPoint
from .organization import Organization
from .person import Person
from .place import Place
from .postal_address import PostalAddress
from .text import Text
from .thing import Thing
from .time import Time
from .virtual_location import VirtualLocation


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
