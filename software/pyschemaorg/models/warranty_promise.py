# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.596184
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.quantitative_value import QuantitativeValue
from models.structured_value import StructuredValue
from models.warranty_scope import WarrantyScope


@dataclass
class WarrantyPromise(StructuredValue):
    durationOfWarranty: QuantitativeValue | None
    warrantyScope: WarrantyScope | None
