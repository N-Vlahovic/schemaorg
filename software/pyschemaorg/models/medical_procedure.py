# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573970
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.event_status_type import EventStatusType
from models.medical_entity import MedicalEntity
from models.medical_procedure_type import MedicalProcedureType
from models.medical_study_status import MedicalStudyStatus
from models.text import Text


@dataclass
class MedicalProcedure(MedicalEntity):
    bodyLocation: Text | None
    followup: Text | None
    howPerformed: Text | None
    preparation: MedicalEntity | Text | None
    procedureType: MedicalProcedureType | None
    status: EventStatusType | MedicalStudyStatus | Text | None
