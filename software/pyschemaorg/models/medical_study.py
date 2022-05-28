# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.603240
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .event_status_type import EventStatusType
from .medical_condition import MedicalCondition
from .medical_entity import MedicalEntity
from .medical_study_status import MedicalStudyStatus
from .organization import Organization
from .person import Person
from .text import Text


@dataclass
class MedicalStudy(MedicalEntity):
    healthCondition: MedicalCondition | None
    sponsor: Organization | Person | None
    status: EventStatusType | MedicalStudyStatus | Text | None
    studyLocation: AdministrativeArea | None
    studySubject: MedicalEntity | None
