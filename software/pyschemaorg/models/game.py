# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.588475
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.place import Place
from models.postal_address import PostalAddress
from models.quantitative_value import QuantitativeValue
from models.thing import Thing
from models.url import URL


@dataclass
class Game(CreativeWork):
    characterAttribute: Thing | None
    gameItem: Thing | None
    gameLocation: Place | PostalAddress | URL | None
    numberOfPlayers: QuantitativeValue | None
    quest: Thing | None
