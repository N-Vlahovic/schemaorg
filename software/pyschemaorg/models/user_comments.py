# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.614462
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .date import Date
from .date_time import DateTime
from .organization import Organization
from .person import Person
from .text import Text
from .url import URL
from .user_interaction import UserInteraction


@dataclass
class UserComments(UserInteraction):
    commentText: Text | None
    commentTime: Date | DateTime | None
    creator: Organization | Person | None
    discusses: CreativeWork | None
    replyToUrl: URL | None
