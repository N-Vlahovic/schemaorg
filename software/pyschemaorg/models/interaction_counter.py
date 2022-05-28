# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.611842
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .action import Action
from .date_time import DateTime
from .integer import Integer
from .place import Place
from .postal_address import PostalAddress
from .software_application import SoftwareApplication
from .structured_value import StructuredValue
from .text import Text
from .time import Time
from .virtual_location import VirtualLocation
from .web_site import WebSite


@dataclass
class InteractionCounter(StructuredValue):
    endTime: DateTime | Time | None
    interactionService: SoftwareApplication | WebSite | None
    interactionType: Action | None
    location: Place | PostalAddress | Text | VirtualLocation | None
    startTime: DateTime | Time | None
    userInteractionCount: Integer | None
