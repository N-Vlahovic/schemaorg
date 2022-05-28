# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.625991
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .data_feed_item import DataFeedItem
from .dataset import Dataset
from .text import Text
from .thing import Thing


@dataclass
class DataFeed(Dataset):
    dataFeedElement: DataFeedItem | Text | Thing | None
