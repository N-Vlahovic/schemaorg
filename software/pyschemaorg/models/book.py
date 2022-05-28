# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.579792
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .book_format_type import BookFormatType
from .boolean import Boolean
from .creative_work import CreativeWork
from .integer import Integer
from .person import Person
from .text import Text


@dataclass
class Book(CreativeWork):
    abridged: Boolean | None
    bookEdition: Text | None
    bookFormat: BookFormatType | None
    illustrator: Person | None
    isbn: Text | None
    numberOfPages: Integer | None
