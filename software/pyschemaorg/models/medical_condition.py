# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.602659
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .anatomical_structure import AnatomicalStructure
from .anatomical_system import AnatomicalSystem
from .d_dx_element import DDxElement
from .drug import Drug
from .event_status_type import EventStatusType
from .medical_condition_stage import MedicalConditionStage
from .medical_entity import MedicalEntity
from .medical_risk_factor import MedicalRiskFactor
from .medical_sign_or_symptom import MedicalSignOrSymptom
from .medical_study_status import MedicalStudyStatus
from .medical_test import MedicalTest
from .medical_therapy import MedicalTherapy
from .superficial_anatomy import SuperficialAnatomy
from .text import Text


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
