# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.601135
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.local_business import LocalBusiness
from models.medical_business import MedicalBusiness
from models.medical_organization import MedicalOrganization


@dataclass
class Dentist(LocalBusiness, MedicalBusiness, MedicalOrganization):
    pass
