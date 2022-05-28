# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577953
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.defined_term import DefinedTerm
from models.enumeration import Enumeration
from models.measurement_type_enumeration import MeasurementTypeEnumeration
from models.property_value import PropertyValue
from models.quantitative_value import QuantitativeValue
from models.structured_value import StructuredValue
from models.text import Text


@dataclass
class QualitativeValue(Enumeration):
    additionalProperty: PropertyValue | None
    equal: QualitativeValue | None
    greater: QualitativeValue | None
    greaterOrEqual: QualitativeValue | None
    lesser: QualitativeValue | None
    lesserOrEqual: QualitativeValue | None
    nonEqual: QualitativeValue | None
    valueReference: DefinedTerm | Enumeration | MeasurementTypeEnumeration | PropertyValue | QualitativeValue | QuantitativeValue | StructuredValue | Text | None
