# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.614021
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .comment import Comment
from .communicate_action import CommunicateAction


@dataclass
class ReplyAction(CommunicateAction):
    resultComment: Comment | None
