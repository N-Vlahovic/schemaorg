# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575096
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.eu_energy_efficiency_enumeration import EUEnergyEfficiencyEnumeration
from models.energy_efficiency_enumeration import EnergyEfficiencyEnumeration
from models.intangible import Intangible


@dataclass
class EnergyConsumptionDetails(Intangible):
    energyEfficiencyScaleMax: EUEnergyEfficiencyEnumeration | None
    energyEfficiencyScaleMin: EUEnergyEfficiencyEnumeration | None
    hasEnergyEfficiencyCategory: EnergyEfficiencyEnumeration | None
