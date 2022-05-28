# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.581542
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .date import Date
from .date_time import DateTime
from .number import Number
from .structured_value import StructuredValue
from .text import Text


@dataclass
class CDCPMDRecord(StructuredValue):
    cvdCollectionDate: DateTime | Text | None
    cvdFacilityCounty: Text | None
    cvdFacilityId: Text | None
    cvdNumBeds: Number | None
    cvdNumBedsOcc: Number | None
    cvdNumC19Died: Number | None
    cvdNumC19HOPats: Number | None
    cvdNumC19HospPats: Number | None
    cvdNumC19MechVentPats: Number | None
    cvdNumC19OFMechVentPats: Number | None
    cvdNumC19OverflowPats: Number | None
    cvdNumICUBeds: Number | None
    cvdNumICUBedsOcc: Number | None
    cvdNumTotBeds: Number | None
    cvdNumVent: Number | None
    cvdNumVentUse: Number | None
    datePosted: Date | DateTime | None
