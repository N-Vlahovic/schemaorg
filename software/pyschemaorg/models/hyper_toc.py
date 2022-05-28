# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.605286
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .hyper_toc_entry import HyperTocEntry
from .media_object import MediaObject


@dataclass
class HyperToc(CreativeWork):
    associatedMedia: MediaObject | None
    tocEntry: HyperTocEntry | None
