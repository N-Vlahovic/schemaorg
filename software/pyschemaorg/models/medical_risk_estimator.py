# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.611143
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .medical_entity import MedicalEntity
from .medical_risk_factor import MedicalRiskFactor


@dataclass
class MedicalRiskEstimator(MedicalEntity):
    estimatesRiskOf: MedicalEntity | None
    includedRiskFactor: MedicalRiskFactor | None
