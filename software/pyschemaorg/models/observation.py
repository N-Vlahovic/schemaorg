# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.590747
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.data_type import DataType
from models.date_time import DateTime
from models.intangible import Intangible
from models.property import Property
from models.quantitative_value import QuantitativeValue
from models.statistical_population import StatisticalPopulation


@dataclass
class Observation(Intangible):
    marginOfError: QuantitativeValue | None
    measuredProperty: Property | None
    measuredValue: DataType | None
    observationDate: DateTime | None
    observedNode: StatisticalPopulation | None
