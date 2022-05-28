# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577899
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.defined_term import DefinedTerm
from models.enumeration import Enumeration
from models.measurement_type_enumeration import MeasurementTypeEnumeration
from models.number import Number
from models.qualitative_value import QualitativeValue
from models.quantitative_value import QuantitativeValue
from models.structured_value import StructuredValue
from models.text import Text
from models.url import URL


@dataclass
class PropertyValue(StructuredValue):
    maxValue: Number | None
    measurementTechnique: Text | URL | None
    minValue: Number | None
    propertyID: Text | URL | None
    unitCode: Text | URL | None
    unitText: Text | None
    value: Boolean | Number | StructuredValue | Text | None
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | Text | None
