# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.606452
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .place import Place
from .postal_address import PostalAddress
from .quantitative_value import QuantitativeValue
from .thing import Thing
from .url import URL


@dataclass
class Game(CreativeWork):
    characterAttribute: Thing | None
    gameItem: Thing | None
    gameLocation: Place | PostalAddress | URL | None
    numberOfPlayers: QuantitativeValue | None
    quest: Thing | None
