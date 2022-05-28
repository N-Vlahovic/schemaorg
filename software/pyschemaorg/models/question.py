# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.623342
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .answer import Answer
from .comment import Comment
from .integer import Integer
from .item_list import ItemList
from .text import Text


@dataclass
class Question(Comment):
    acceptedAnswer: Answer | ItemList | None
    answerCount: Integer | None
    eduQuestionType: Text | None
    suggestedAnswer: Answer | ItemList | None
