# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.587508
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.duration import Duration
from models.how_to_supply import HowToSupply
from models.how_to_tool import HowToTool
from models.list_item import ListItem
from models.media_object import MediaObject
from models.text import Text
from models.url import URL


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
