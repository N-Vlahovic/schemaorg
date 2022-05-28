# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582308
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.anatomical_structure import AnatomicalStructure
from models.brain_structure import BrainStructure
from models.muscle import Muscle
from models.superficial_anatomy import SuperficialAnatomy


@dataclass
class Nerve(AnatomicalStructure):
    branch: AnatomicalStructure | None
    nerveMotor: Muscle | None
    sensoryUnit: AnatomicalStructure | SuperficialAnatomy | None
    sourcedFrom: BrainStructure | None
