# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574347
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date import Date
from models.date_time import DateTime
from models.number import Number
from models.structured_value import StructuredValue
from models.text import Text


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
