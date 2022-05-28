# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578186
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.dose_schedule import DoseSchedule
from models.drug_class import DrugClass
from models.drug_legal_status import DrugLegalStatus
from models.drug_pregnancy_category import DrugPregnancyCategory
from models.drug_prescription_status import DrugPrescriptionStatus
from models.drug_strength import DrugStrength
from models.health_insurance_plan import HealthInsurancePlan
from models.maximum_dose_schedule import MaximumDoseSchedule
from models.medical_enumeration import MedicalEnumeration
from models.organization import Organization
from models.substance import Substance
from models.text import Text
from models.url import URL


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
