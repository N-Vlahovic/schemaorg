# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.604933
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .duration import Duration
from .how_to_supply import HowToSupply
from .how_to_tool import HowToTool
from .list_item import ListItem
from .media_object import MediaObject
from .text import Text
from .url import URL


@dataclass
class HowToDirection(CreativeWork, ListItem):
    afterMedia: MediaObject | URL | None
    beforeMedia: MediaObject | URL | None
    duringMedia: MediaObject | URL | None
    performTime: Duration | None
    prepTime: Duration | None
    supply: HowToSupply | Text | None
    tool: HowToTool | Text | None
    totalTime: Duration | None
