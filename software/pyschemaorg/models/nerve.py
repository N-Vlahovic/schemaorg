# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.596123
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .anatomical_structure import AnatomicalStructure
from .brain_structure import BrainStructure
from .muscle import Muscle
from .superficial_anatomy import SuperficialAnatomy


@dataclass
class Nerve(AnatomicalStructure):
    branch: AnatomicalStructure | None
    nerveMotor: Muscle | None
    sensoryUnit: AnatomicalStructure | SuperficialAnatomy | None
    sourcedFrom: BrainStructure | None
