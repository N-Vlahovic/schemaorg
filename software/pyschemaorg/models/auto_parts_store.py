# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.583406
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.automotive_business import AutomotiveBusiness
from models.store import Store


@dataclass
class AutoPartsStore(AutomotiveBusiness, Store):
    pass
