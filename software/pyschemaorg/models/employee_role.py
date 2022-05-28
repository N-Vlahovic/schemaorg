# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.595763
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.monetary_amount import MonetaryAmount
from models.number import Number
from models.organization_role import OrganizationRole
from models.price_specification import PriceSpecification
from models.text import Text


@dataclass
class EmployeeRole(OrganizationRole):
    baseSalary: MonetaryAmount | Number | PriceSpecification | None
    salaryCurrency: Text | None
