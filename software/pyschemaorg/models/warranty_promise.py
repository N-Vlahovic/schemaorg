# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.619418
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .quantitative_value import QuantitativeValue
from .structured_value import StructuredValue
from .warranty_scope import WarrantyScope


@dataclass
class WarrantyPromise(StructuredValue):
    durationOfWarranty: QuantitativeValue | None
    warrantyScope: WarrantyScope | None
