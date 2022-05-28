# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581868
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.audience import Audience
from models.language import Language
from models.place import Place
from models.text import Text


@dataclass
class TouristAttraction(Place):
    availableLanguage: Language | Text | None
    touristType: Audience | Text | None
