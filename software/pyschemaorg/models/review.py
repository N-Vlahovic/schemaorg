# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.593742
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .item_list import ItemList
from .list_item import ListItem
from .rating import Rating
from .text import Text
from .thing import Thing
from .web_content import WebContent


@dataclass
class Review(CreativeWork):
    associatedClaimReview: Review | None
    associatedMediaReview: Review | None
    associatedReview: Review | None
    itemReviewed: Thing | None
    negativeNotes: ItemList | ListItem | Text | WebContent | None
    positiveNotes: ItemList | ListItem | Text | WebContent | None
    reviewAspect: Text | None
    reviewBody: Text | None
    reviewRating: Rating | None
