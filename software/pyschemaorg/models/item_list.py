# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.584606
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.intangible import Intangible
from models.integer import Integer
from models.item_list_order_type import ItemListOrderType
from models.list_item import ListItem
from models.text import Text
from models.thing import Thing


@dataclass
class ItemList(Intangible):
    itemListElement: ListItem | Text | Thing | None
    itemListOrder: ItemListOrderType | Text | None
    numberOfItems: Integer | None
