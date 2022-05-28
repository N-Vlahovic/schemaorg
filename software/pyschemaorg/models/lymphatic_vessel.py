# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.591091
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .anatomical_structure import AnatomicalStructure
from .anatomical_system import AnatomicalSystem
from .vessel import Vessel


@dataclass
class LymphaticVessel(Vessel):
    originatesFrom: Vessel | None
    regionDrained: AnatomicalStructure | AnatomicalSystem | None
    runsTo: Vessel | None
