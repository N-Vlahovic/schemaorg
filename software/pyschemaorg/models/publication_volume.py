# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.590672
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.integer import Integer
from models.text import Text


@dataclass
class PublicationVolume(CreativeWork):
    pageEnd: Integer | Text | None
    pageStart: Integer | Text | None
    pagination: Text | None
    volumeNumber: Integer | Text | None
