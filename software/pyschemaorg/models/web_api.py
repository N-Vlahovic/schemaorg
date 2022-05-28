# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.589690
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.service import Service
from models.url import URL


@dataclass
class WebAPI(Service):
    documentation: CreativeWork | URL | None
