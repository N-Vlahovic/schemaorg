# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.581522
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.media_object import MediaObject
from models.property_value import PropertyValue
from models.text import Text


@dataclass
class ImageObject(MediaObject):
    caption: MediaObject | Text | None
    embeddedTextCaption: Text | None
    exifData: PropertyValue | Text | None
    representativeOfPage: Boolean | None
    thumbnail: ImageObject | None
