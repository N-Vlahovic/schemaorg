# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.611264
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .event import Event
from .language import Language
from .publication_event import PublicationEvent
from .text import Text


@dataclass
class BroadcastEvent(PublicationEvent):
    broadcastOfEvent: Event | None
    isLiveBroadcast: Boolean | None
    subtitleLanguage: Language | Text | None
    videoFormat: Text | None
