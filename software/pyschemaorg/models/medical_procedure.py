# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.580802
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .event_status_type import EventStatusType
from .medical_entity import MedicalEntity
from .medical_procedure_type import MedicalProcedureType
from .medical_study_status import MedicalStudyStatus
from .text import Text


@dataclass
class MedicalProcedure(MedicalEntity):
    bodyLocation: Text | None
    followup: Text | None
    howPerformed: Text | None
    preparation: MedicalEntity | Text | None
    procedureType: MedicalProcedureType | None
    status: EventStatusType | MedicalStudyStatus | Text | None
