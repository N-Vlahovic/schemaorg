# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.601573
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .contact_point import ContactPoint
from .health_plan_formulary import HealthPlanFormulary
from .health_plan_network import HealthPlanNetwork
from .intangible import Intangible
from .text import Text
from .url import URL


@dataclass
class HealthInsurancePlan(Intangible):
    benefitsSummaryUrl: URL | None
    contactPoint: ContactPoint | None
    healthPlanDrugOption: Text | None
    healthPlanDrugTier: Text | None
    healthPlanId: Text | None
    healthPlanMarketingUrl: URL | None
    includesHealthPlanFormulary: HealthPlanFormulary | None
    includesHealthPlanNetwork: HealthPlanNetwork | None
    usesHealthPlanIdStandard: Text | URL | None
