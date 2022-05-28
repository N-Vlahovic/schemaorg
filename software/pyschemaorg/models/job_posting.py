# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.580488
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .boolean import Boolean
from .category_code import CategoryCode
from .contact_point import ContactPoint
from .date import Date
from .date_time import DateTime
from .defined_term import DefinedTerm
from .educational_occupational_credential import EducationalOccupationalCredential
from .intangible import Intangible
from .integer import Integer
from .monetary_amount import MonetaryAmount
from .monetary_amount_distribution import MonetaryAmountDistribution
from .number import Number
from .occupation import Occupation
from .occupational_experience_requirements import OccupationalExperienceRequirements
from .organization import Organization
from .place import Place
from .price_specification import PriceSpecification
from .text import Text
from .url import URL


@dataclass
class JobPosting(Intangible):
    applicantLocationRequirements: AdministrativeArea | None
    applicationContact: ContactPoint | None
    baseSalary: MonetaryAmount | Number | PriceSpecification | None
    benefits: Text | None
    datePosted: Date | DateTime | None
    directApply: Boolean | None
    educationRequirements: EducationalOccupationalCredential | Text | None
    eligibilityToWorkRequirement: Text | None
    employerOverview: Text | None
    employmentType: Text | None
    employmentUnit: Organization | None
    estimatedSalary: MonetaryAmount | MonetaryAmountDistribution | Number | None
    experienceInPlaceOfEducation: Boolean | None
    experienceRequirements: OccupationalExperienceRequirements | Text | None
    hiringOrganization: Organization | None
    incentiveCompensation: Text | None
    incentives: Text | None
    industry: DefinedTerm | Text | None
    jobBenefits: Text | None
    jobImmediateStart: Boolean | None
    jobLocation: Place | None
    jobLocationType: Text | None
    jobStartDate: Date | Text | None
    occupationalCategory: CategoryCode | Text | None
    physicalRequirement: DefinedTerm | Text | URL | None
    qualifications: EducationalOccupationalCredential | Text | None
    relevantOccupation: Occupation | None
    responsibilities: Text | None
    salaryCurrency: Text | None
    securityClearanceRequirement: Text | URL | None
    sensoryRequirement: DefinedTerm | Text | URL | None
    skills: DefinedTerm | Text | None
    specialCommitments: Text | None
    title: Text | None
    totalJobOpenings: Integer | None
    validThrough: Date | DateTime | None
    workHours: Text | None
