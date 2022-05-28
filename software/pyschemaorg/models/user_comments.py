# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.593345
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.date import Date
from models.date_time import DateTime
from models.organization import Organization
from models.person import Person
from models.text import Text
from models.url import URL
from models.user_interaction import UserInteraction


@dataclass
class UserComments(UserInteraction):
    commentText: Text | None
    commentTime: Date | DateTime | None
    creator: Organization | Person | None
    discusses: CreativeWork | None
    replyToUrl: URL | None
