# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575995
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date_time import DateTime
from models.organize_action import OrganizeAction


@dataclass
class PlanAction(OrganizeAction):
    scheduledTime: DateTime | None
