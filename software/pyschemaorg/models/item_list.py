# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.599956
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .intangible import Intangible
from .integer import Integer
from .item_list_order_type import ItemListOrderType
from .list_item import ListItem
from .text import Text
from .thing import Thing


@dataclass
class ItemList(Intangible):
    itemListElement: ListItem | Text | Thing | None
    itemListOrder: ItemListOrderType | Text | None
    numberOfItems: Integer | None
