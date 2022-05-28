# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.595130
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.item_list import ItemList
from models.list_item import ListItem
from models.text import Text


@dataclass
class HowToSection(CreativeWork, ItemList, ListItem):
    steps: CreativeWork | ItemList | Text | None
