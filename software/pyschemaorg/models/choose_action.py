# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.611438
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .assess_action import AssessAction
from .text import Text
from .thing import Thing


@dataclass
class ChooseAction(AssessAction):
    actionOption: Text | Thing | None
    option: Text | Thing | None
