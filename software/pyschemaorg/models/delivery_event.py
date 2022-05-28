# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582383
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.date_time import DateTime
from models.delivery_method import DeliveryMethod
from models.event import Event
from models.text import Text


@dataclass
class DeliveryEvent(Event):
    accessCode: Text | None
    availableFrom: DateTime | None
    availableThrough: DateTime | None
    hasDeliveryMethod: DeliveryMethod | None
