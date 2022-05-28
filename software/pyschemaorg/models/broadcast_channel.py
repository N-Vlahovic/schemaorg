# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.607198
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .broadcast_frequency_specification import BroadcastFrequencySpecification
from .broadcast_service import BroadcastService
from .cable_or_satellite_service import CableOrSatelliteService
from .intangible import Intangible
from .text import Text
from .url import URL


@dataclass
class BroadcastChannel(Intangible):
    broadcastChannelId: Text | None
    broadcastFrequency: BroadcastFrequencySpecification | Text | None
    broadcastServiceTier: Text | None
    genre: Text | URL | None
    inBroadcastLineup: CableOrSatelliteService | None
    providesBroadcastService: BroadcastService | None
