# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.604013
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .abstract_base import AbstractBase
from .action import Action
from .creative_work import CreativeWork
from .event import Event
from .image_object import ImageObject
from .property_value import PropertyValue
from .text import Text
from .url import URL


@dataclass
class Thing(AbstractBase):
    additionalType: URL | None
    alternateName: Text | None
    description: Text | None
    disambiguatingDescription: Text | None
    identifier: PropertyValue | Text | URL | None
    image: ImageObject | URL | None
    mainEntityOfPage: CreativeWork | URL | None
    name: Text | None
    potentialAction: Action | None
    sameAs: URL | None
    subjectOf: CreativeWork | Event | None
    url: URL | None
