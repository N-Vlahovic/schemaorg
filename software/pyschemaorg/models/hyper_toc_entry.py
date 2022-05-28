# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.587023
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.media_object import MediaObject
from models.text import Text


@dataclass
class HyperTocEntry(CreativeWork):
    associatedMedia: MediaObject | None
    tocContinuation: HyperTocEntry | None
    utterances: Text | None
