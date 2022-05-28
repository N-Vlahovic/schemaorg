# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581656
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.drug_cost_category import DrugCostCategory
from models.medical_entity import MedicalEntity
from models.number import Number
from models.qualitative_value import QualitativeValue
from models.text import Text


@dataclass
class DrugCost(MedicalEntity):
    applicableLocation: AdministrativeArea | None
    costCategory: DrugCostCategory | None
    costCurrency: Text | None
    costOrigin: Text | None
    costPerUnit: Number | QualitativeValue | Text | None
    drugUnit: Text | None
