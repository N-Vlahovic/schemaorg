# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.599713
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.data_feed_item import DataFeedItem
from models.dataset import Dataset
from models.text import Text
from models.thing import Thing


@dataclass
class DataFeed(Dataset):
    dataFeedElement: DataFeedItem | Text | Thing | None
