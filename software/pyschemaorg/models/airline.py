# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579257
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boarding_policy_type import BoardingPolicyType
from models.organization import Organization
from models.text import Text


@dataclass
class Airline(Organization):
    boardingPolicy: BoardingPolicyType | None
    iataCode: Text | None
