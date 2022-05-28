# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.586454
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.event_status_type import EventStatusType
from models.medical_condition import MedicalCondition
from models.medical_entity import MedicalEntity
from models.medical_study_status import MedicalStudyStatus
from models.organization import Organization
from models.person import Person
from models.text import Text


@dataclass
class MedicalStudy(MedicalEntity):
    healthCondition: MedicalCondition | None
    sponsor: Organization | Person | None
    status: EventStatusType | MedicalStudyStatus | Text | None
    studyLocation: AdministrativeArea | None
    studySubject: MedicalEntity | None
