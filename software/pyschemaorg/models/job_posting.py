# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573787
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.boolean import Boolean
from models.category_code import CategoryCode
from models.contact_point import ContactPoint
from models.date import Date
from models.date_time import DateTime
from models.defined_term import DefinedTerm
from models.educational_occupational_credential import EducationalOccupationalCredential
from models.intangible import Intangible
from models.integer import Integer
from models.monetary_amount import MonetaryAmount
from models.monetary_amount_distribution import MonetaryAmountDistribution
from models.number import Number
from models.occupation import Occupation
from models.occupational_experience_requirements import OccupationalExperienceRequirements
from models.organization import Organization
from models.place import Place
from models.price_specification import PriceSpecification
from models.text import Text
from models.url import URL


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
