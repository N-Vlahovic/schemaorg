# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.608313
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .anatomical_structure import AnatomicalStructure
from .nerve import Nerve
from .text import Text
from .vessel import Vessel


@dataclass
class Muscle(AnatomicalStructure):
    antagonist: Muscle | None
    bloodSupply: Vessel | None
    insertion: AnatomicalStructure | None
    muscleAction: Text | None
    nerve: Nerve | None
