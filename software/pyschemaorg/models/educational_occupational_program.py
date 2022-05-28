# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576098
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.alignment_object import AlignmentObject
from models.category_code import CategoryCode
from models.course import Course
from models.date import Date
from models.date_time import DateTime
from models.day_of_week import DayOfWeek
from models.defined_term import DefinedTerm
from models.demand import Demand
from models.duration import Duration
from models.educational_occupational_credential import EducationalOccupationalCredential
from models.intangible import Intangible
from models.integer import Integer
from models.monetary_amount_distribution import MonetaryAmountDistribution
from models.number import Number
from models.offer import Offer
from models.organization import Organization
from models.person import Person
from models.structured_value import StructuredValue
from models.text import Text
from models.url import URL


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
