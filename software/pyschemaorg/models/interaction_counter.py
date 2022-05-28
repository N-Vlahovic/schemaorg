# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.591805
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.action import Action
from models.date_time import DateTime
from models.integer import Integer
from models.place import Place
from models.postal_address import PostalAddress
from models.software_application import SoftwareApplication
from models.structured_value import StructuredValue
from models.text import Text
from models.time import Time
from models.virtual_location import VirtualLocation
from models.web_site import WebSite


@dataclass
class InteractionCounter(StructuredValue):
    endTime: DateTime | Time | None
    interactionService: SoftwareApplication | WebSite | None
    interactionType: Action | None
    location: Place | PostalAddress | Text | VirtualLocation | None
    startTime: DateTime | Time | None
    userInteractionCount: Integer | None
