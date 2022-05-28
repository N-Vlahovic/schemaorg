# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.585499
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.contact_point import ContactPoint
from models.health_plan_formulary import HealthPlanFormulary
from models.health_plan_network import HealthPlanNetwork
from models.intangible import Intangible
from models.text import Text
from models.url import URL


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
