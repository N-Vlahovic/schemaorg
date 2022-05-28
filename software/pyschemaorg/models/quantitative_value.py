# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.588703
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .defined_term import DefinedTerm
from .enumeration import Enumeration
from .measurement_type_enumeration import MeasurementTypeEnumeration
from .number import Number
from .property_value import PropertyValue
from .qualitative_value import QualitativeValue
from .structured_value import StructuredValue
from .text import Text
from .url import URL


@dataclass
class QuantitativeValue(StructuredValue):
    additionalProperty: PropertyValue | None
    maxValue: Number | None
    minValue: Number | None
    unitCode: Text | URL | None
    unitText: Text | None
    value: Boolean | Number | StructuredValue | Text | None
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | Text | None
