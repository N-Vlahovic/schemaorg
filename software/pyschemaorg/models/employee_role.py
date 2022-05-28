# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.618656
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .monetary_amount import MonetaryAmount
from .number import Number
from .organization_role import OrganizationRole
from .price_specification import PriceSpecification
from .text import Text


@dataclass
class EmployeeRole(OrganizationRole):
    baseSalary: MonetaryAmount | Number | PriceSpecification | None
    salaryCurrency: Text | None
