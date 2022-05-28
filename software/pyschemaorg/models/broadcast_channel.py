# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.588908
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.broadcast_frequency_specification import BroadcastFrequencySpecification
from models.broadcast_service import BroadcastService
from models.cable_or_satellite_service import CableOrSatelliteService
from models.intangible import Intangible
from models.text import Text
from models.url import URL


@dataclass
class BroadcastChannel(Intangible):
    broadcastChannelId: Text | None
    broadcastFrequency: BroadcastFrequencySpecification | Text | None
    broadcastServiceTier: Text | None
    genre: Text | URL | None
    inBroadcastLineup: CableOrSatelliteService | None
    providesBroadcastService: BroadcastService | None
