# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.598429
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .audience import Audience
from .contact_point import ContactPoint
from .interact_action import InteractAction
from .language import Language
from .organization import Organization
from .person import Person
from .text import Text
from .thing import Thing


@dataclass
class CommunicateAction(InteractAction):
    about: Thing | None
    inLanguage: Language | Text | None
    language: Language | None
    recipient: Audience | ContactPoint | Organization | Person | None
