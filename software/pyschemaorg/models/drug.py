# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.589064
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .dose_schedule import DoseSchedule
from .drug_class import DrugClass
from .drug_legal_status import DrugLegalStatus
from .drug_pregnancy_category import DrugPregnancyCategory
from .drug_prescription_status import DrugPrescriptionStatus
from .drug_strength import DrugStrength
from .health_insurance_plan import HealthInsurancePlan
from .maximum_dose_schedule import MaximumDoseSchedule
from .medical_enumeration import MedicalEnumeration
from .organization import Organization
from .substance import Substance
from .text import Text
from .url import URL


@dataclass
class Drug(Substance):
    activeIngredient: Text | None
    administrationRoute: Text | None
    alcoholWarning: Text | None
    availableStrength: DrugStrength | None
    breastfeedingWarning: Text | None
    clincalPharmacology: Text | None
    clinicalPharmacology: Text | None
    dosageForm: Text | None
    doseSchedule: DoseSchedule | None
    drugClass: DrugClass | None
    drugUnit: Text | None
    foodWarning: Text | None
    includedInHealthInsurancePlan: HealthInsurancePlan | None
    interactingDrug: Drug | None
    isAvailableGenerically: Boolean | None
    isProprietary: Boolean | None
    labelDetails: URL | None
    legalStatus: DrugLegalStatus | MedicalEnumeration | Text | None
    manufacturer: Organization | None
    maximumIntake: MaximumDoseSchedule | None
    mechanismOfAction: Text | None
    nonProprietaryName: Text | None
    overdosage: Text | None
    pregnancyCategory: DrugPregnancyCategory | None
    pregnancyWarning: Text | None
    prescribingInfo: URL | None
    prescriptionStatus: DrugPrescriptionStatus | Text | None
    proprietaryName: Text | None
    relatedDrug: Drug | None
    rxcui: Text | None
    warning: Text | URL | None
