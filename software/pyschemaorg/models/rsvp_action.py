# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.582709
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .comment import Comment
from .inform_action import InformAction
from .number import Number
from .rsvp_response_type import RsvpResponseType


@dataclass
class RsvpAction(InformAction):
    additionalNumberOfGuests: Number | None
    comment: Comment | None
    rsvpResponse: RsvpResponseType | None
