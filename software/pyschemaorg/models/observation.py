# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.610449
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .data_type import DataType
from .date_time import DateTime
from .intangible import Intangible
from .property import Property
from .quantitative_value import QuantitativeValue
from .statistical_population import StatisticalPopulation


@dataclass
class Observation(Intangible):
    marginOfError: QuantitativeValue | None
    measuredProperty: Property | None
    measuredValue: DataType | None
    observationDate: DateTime | None
    observedNode: StatisticalPopulation | None
