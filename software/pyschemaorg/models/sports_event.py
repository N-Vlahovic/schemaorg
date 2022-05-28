# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582638
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .event import Event
from .person import Person
from .sports_team import SportsTeam
from .text import Text
from .url import URL


@dataclass
class SportsEvent(Event):
    awayTeam: Person | SportsTeam | None
    competitor: Person | SportsTeam | None
    homeTeam: Person | SportsTeam | None
    sport: Text | URL | None
