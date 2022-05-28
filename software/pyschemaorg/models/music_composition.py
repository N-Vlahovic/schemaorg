# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.592114
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .event import Event
from .music_recording import MusicRecording
from .organization import Organization
from .person import Person
from .text import Text


@dataclass
class MusicComposition(CreativeWork):
    composer: Organization | Person | None
    firstPerformance: Event | None
    includedComposition: MusicComposition | None
    iswcCode: Text | None
    lyricist: Person | None
    lyrics: CreativeWork | None
    musicArrangement: MusicComposition | None
    musicCompositionForm: Text | None
    musicalKey: Text | None
    recordedAs: MusicRecording | None
