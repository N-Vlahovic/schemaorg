# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.594843
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .media_object import MediaObject
from .property_value import PropertyValue
from .text import Text


@dataclass
class ImageObject(MediaObject):
    caption: MediaObject | Text | None
    embeddedTextCaption: Text | None
    exifData: PropertyValue | Text | None
    representativeOfPage: Boolean | None
    thumbnail: ImageObject | None
