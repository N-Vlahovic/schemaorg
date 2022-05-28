# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.584036
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .action import Action
from .audience import Audience
from .event import Event


@dataclass
class PlayAction(Action):
    audience: Audience | None
    event: Event | None
