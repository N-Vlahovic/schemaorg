# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.579005
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.delivery_method import DeliveryMethod
from models.find_action import FindAction


@dataclass
class TrackAction(FindAction):
    deliveryMethod: DeliveryMethod | None
