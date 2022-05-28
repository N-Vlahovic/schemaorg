# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.598177
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.answer import Answer
from models.comment import Comment
from models.integer import Integer
from models.item_list import ItemList
from models.text import Text


@dataclass
class Question(Comment):
    acceptedAnswer: Answer | ItemList | None
    answerCount: Integer | None
    eduQuestionType: Text | None
    suggestedAnswer: Answer | ItemList | None
