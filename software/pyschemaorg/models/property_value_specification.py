# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582044
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.intangible import Intangible
from models.number import Number
from models.text import Text
from models.thing import Thing


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
