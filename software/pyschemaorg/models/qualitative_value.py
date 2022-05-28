# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.588576
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .defined_term import DefinedTerm
from .enumeration import Enumeration
from .measurement_type_enumeration import MeasurementTypeEnumeration
from .property_value import PropertyValue
from .quantitative_value import QuantitativeValue
from .structured_value import StructuredValue
from .text import Text


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
