# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.586081
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.anatomical_structure import AnatomicalStructure
from models.anatomical_system import AnatomicalSystem
from models.d_dx_element import DDxElement
from models.drug import Drug
from models.event_status_type import EventStatusType
from models.medical_condition_stage import MedicalConditionStage
from models.medical_entity import MedicalEntity
from models.medical_risk_factor import MedicalRiskFactor
from models.medical_sign_or_symptom import MedicalSignOrSymptom
from models.medical_study_status import MedicalStudyStatus
from models.medical_test import MedicalTest
from models.medical_therapy import MedicalTherapy
from models.superficial_anatomy import SuperficialAnatomy
from models.text import Text


@dataclass
class MedicalCondition(MedicalEntity):
    associatedAnatomy: AnatomicalStructure | AnatomicalSystem | SuperficialAnatomy | None
    differentialDiagnosis: DDxElement | None
    drug: Drug | None
    epidemiology: Text | None
    expectedPrognosis: Text | None
    naturalProgression: Text | None
    pathophysiology: Text | None
    possibleComplication: Text | None
    possibleTreatment: MedicalTherapy | None
    primaryPrevention: MedicalTherapy | None
    riskFactor: MedicalRiskFactor | None
    secondaryPrevention: MedicalTherapy | None
    signOrSymptom: MedicalSignOrSymptom | None
    stage: MedicalConditionStage | None
    status: EventStatusType | MedicalStudyStatus | Text | None
    typicalTest: MedicalTest | None
