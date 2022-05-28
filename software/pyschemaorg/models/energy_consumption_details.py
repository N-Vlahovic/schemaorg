# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582921
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .eu_energy_efficiency_enumeration import EUEnergyEfficiencyEnumeration
from .energy_efficiency_enumeration import EnergyEfficiencyEnumeration
from .intangible import Intangible


@dataclass
class EnergyConsumptionDetails(Intangible):
    energyEfficiencyScaleMax: EUEnergyEfficiencyEnumeration | None
    energyEfficiencyScaleMin: EUEnergyEfficiencyEnumeration | None
    hasEnergyEfficiencyCategory: EnergyEfficiencyEnumeration | None
