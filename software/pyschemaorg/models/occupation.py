# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.587245
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .category_code import CategoryCode
from .defined_term import DefinedTerm
from .educational_occupational_credential import EducationalOccupationalCredential
from .intangible import Intangible
from .monetary_amount import MonetaryAmount
from .monetary_amount_distribution import MonetaryAmountDistribution
from .number import Number
from .occupational_experience_requirements import OccupationalExperienceRequirements
from .text import Text


@dataclass
class Occupation(Intangible):
    educationRequirements: EducationalOccupationalCredential | Text | None
    estimatedSalary: MonetaryAmount | MonetaryAmountDistribution | Number | None
    experienceRequirements: OccupationalExperienceRequirements | Text | None
    occupationLocation: AdministrativeArea | None
    occupationalCategory: CategoryCode | Text | None
    qualifications: EducationalOccupationalCredential | Text | None
    responsibilities: Text | None
    skills: DefinedTerm | Text | None
