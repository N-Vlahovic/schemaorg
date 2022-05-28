# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.594680
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.category_code import CategoryCode
from models.educational_occupational_program import EducationalOccupationalProgram
from models.monetary_amount_distribution import MonetaryAmountDistribution
from models.text import Text


@dataclass
class WorkBasedProgram(EducationalOccupationalProgram):
    occupationalCategory: CategoryCode | Text | None
    trainingSalary: MonetaryAmountDistribution | None
