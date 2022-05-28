# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.592790
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.intangible import Intangible
from models.number import Number
from models.qualitative_value import QualitativeValue
from models.quantitative_value import QuantitativeValue
from models.text import Text


@dataclass
class BroadcastFrequencySpecification(Intangible):
    broadcastFrequencyValue: Number | QuantitativeValue | None
    broadcastSignalModulation: QualitativeValue | Text | None
    broadcastSubChannel: Text | None
