# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589827
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.interact_action import InteractAction
from models.organization import Organization
from models.person import Person


@dataclass
class FollowAction(InteractAction):
    followee: Organization | Person | None
