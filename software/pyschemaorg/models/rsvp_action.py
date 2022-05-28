# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574962
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.comment import Comment
from models.inform_action import InformAction
from models.number import Number
from models.rsvp_response_type import RsvpResponseType


@dataclass
class RsvpAction(InformAction):
    additionalNumberOfGuests: Number | None
    comment: Comment | None
    rsvpResponse: RsvpResponseType | None
