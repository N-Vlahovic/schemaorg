# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.581887
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .drug_legal_status import DrugLegalStatus
from .maximum_dose_schedule import MaximumDoseSchedule
from .medical_enumeration import MedicalEnumeration
from .organization import Organization
from .recommended_dose_schedule import RecommendedDoseSchedule
from .substance import Substance
from .text import Text


@dataclass
class DietarySupplement(Substance):
    activeIngredient: Text | None
    isProprietary: Boolean | None
    legalStatus: DrugLegalStatus | MedicalEnumeration | Text | None
    manufacturer: Organization | None
    maximumIntake: MaximumDoseSchedule | None
    mechanismOfAction: Text | None
    nonProprietaryName: Text | None
    proprietaryName: Text | None
    recommendedIntake: RecommendedDoseSchedule | None
    safetyConsideration: Text | None
    targetPopulation: Text | None
