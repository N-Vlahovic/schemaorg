# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.584703
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .alignment_object import AlignmentObject
from .category_code import CategoryCode
from .course import Course
from .date import Date
from .date_time import DateTime
from .day_of_week import DayOfWeek
from .defined_term import DefinedTerm
from .demand import Demand
from .duration import Duration
from .educational_occupational_credential import EducationalOccupationalCredential
from .intangible import Intangible
from .integer import Integer
from .monetary_amount_distribution import MonetaryAmountDistribution
from .number import Number
from .offer import Offer
from .organization import Organization
from .person import Person
from .structured_value import StructuredValue
from .text import Text
from .url import URL


@dataclass
class EducationalOccupationalProgram(Intangible):
    applicationDeadline: Date | None
    applicationStartDate: Date | None
    dayOfWeek: DayOfWeek | None
    educationalCredentialAwarded: EducationalOccupationalCredential | Text | URL | None
    educationalProgramMode: Text | URL | None
    endDate: Date | DateTime | None
    financialAidEligible: DefinedTerm | Text | None
    hasCourse: Course | None
    maximumEnrollment: Integer | None
    numberOfCredits: Integer | StructuredValue | None
    occupationalCategory: CategoryCode | Text | None
    occupationalCredentialAwarded: EducationalOccupationalCredential | Text | URL | None
    offers: Demand | Offer | None
    programPrerequisites: AlignmentObject | Course | EducationalOccupationalCredential | Text | None
    programType: DefinedTerm | Text | None
    provider: Organization | Person | None
    salaryUponCompletion: MonetaryAmountDistribution | None
    startDate: Date | DateTime | None
    termDuration: Duration | None
    termsPerYear: Number | None
    timeOfDay: Text | None
    timeToComplete: Duration | None
    trainingSalary: MonetaryAmountDistribution | None
    typicalCreditsPerTerm: Integer | StructuredValue | None
