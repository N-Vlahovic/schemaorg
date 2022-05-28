# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.577329
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.category_code import CategoryCode
from models.defined_term import DefinedTerm
from models.educational_occupational_credential import EducationalOccupationalCredential
from models.intangible import Intangible
from models.monetary_amount import MonetaryAmount
from models.monetary_amount_distribution import MonetaryAmountDistribution
from models.number import Number
from models.occupational_experience_requirements import OccupationalExperienceRequirements
from models.text import Text


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
