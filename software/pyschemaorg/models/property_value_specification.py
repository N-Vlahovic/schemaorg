# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.595676
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .intangible import Intangible
from .number import Number
from .text import Text
from .thing import Thing


@dataclass
class PropertyValueSpecification(Intangible):
    defaultValue: Text | Thing | None
    maxValue: Number | None
    minValue: Number | None
    multipleValues: Boolean | None
    readonlyValue: Boolean | None
    stepValue: Number | None
    valueMaxLength: Number | None
    valueMinLength: Number | None
    valueName: Text | None
    valuePattern: Text | None
    valueRequired: Boolean | None
