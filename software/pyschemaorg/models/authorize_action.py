# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.598328
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .allocate_action import AllocateAction
from .audience import Audience
from .contact_point import ContactPoint
from .organization import Organization
from .person import Person


@dataclass
class AuthorizeAction(AllocateAction):
    recipient: Audience | ContactPoint | Organization | Person | None
