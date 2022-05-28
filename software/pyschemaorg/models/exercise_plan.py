# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584372
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.duration import Duration
from models.energy import Energy
from models.number import Number
from models.physical_activity import PhysicalActivity
from models.quantitative_value import QuantitativeValue
from models.text import Text


@dataclass
class ExercisePlan(CreativeWork, PhysicalActivity):
    activityDuration: Duration | QuantitativeValue | None
    activityFrequency: QuantitativeValue | Text | None
    additionalVariable: Text | None
    exerciseType: Text | None
    intensity: QuantitativeValue | Text | None
    repetitions: Number | QuantitativeValue | None
    restPeriods: QuantitativeValue | Text | None
    workload: Energy | QuantitativeValue | None
