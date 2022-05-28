# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.613520
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .intangible import Intangible
from .number import Number
from .qualitative_value import QualitativeValue
from .quantitative_value import QuantitativeValue
from .text import Text


@dataclass
class BroadcastFrequencySpecification(Intangible):
    broadcastFrequencyValue: Number | QuantitativeValue | None
    broadcastSignalModulation: QualitativeValue | Text | None
    broadcastSubChannel: Text | None
