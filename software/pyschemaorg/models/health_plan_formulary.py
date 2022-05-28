# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584011
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.intangible import Intangible
from models.text import Text


@dataclass
class HealthPlanFormulary(Intangible):
    healthPlanCostSharing: Boolean | None
    healthPlanDrugTier: Text | None
    offersPrescriptionByMail: Boolean | None
