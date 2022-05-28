# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.586950
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.abstract_base import AbstractBase
from models.action import Action
from models.creative_work import CreativeWork
from models.event import Event
from models.image_object import ImageObject
from models.property_value import PropertyValue
from models.text import Text
from models.url import URL


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
