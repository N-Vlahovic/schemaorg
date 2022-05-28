# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589477
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.broadcast_channel import BroadcastChannel
from models.broadcast_frequency_specification import BroadcastFrequencySpecification
from models.language import Language
from models.organization import Organization
from models.place import Place
from models.service import Service
from models.text import Text


@dataclass
class BroadcastService(Service):
    area: Place | None
    broadcastAffiliateOf: Organization | None
    broadcastDisplayName: Text | None
    broadcastFrequency: BroadcastFrequencySpecification | Text | None
    broadcastTimezone: Text | None
    broadcaster: Organization | None
    callSign: Text | None
    hasBroadcastChannel: BroadcastChannel | None
    inLanguage: Language | Text | None
    parentService: BroadcastService | None
    videoFormat: Text | None
