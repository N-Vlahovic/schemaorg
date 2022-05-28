# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589544
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.anatomical_structure import AnatomicalStructure
from models.nerve import Nerve
from models.text import Text
from models.vessel import Vessel


@dataclass
class Muscle(AnatomicalStructure):
    antagonist: Muscle | None
    bloodSupply: Vessel | None
    insertion: AnatomicalStructure | None
    muscleAction: Text | None
    nerve: Nerve | None
