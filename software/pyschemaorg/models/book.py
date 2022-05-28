# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573411
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.book_format_type import BookFormatType
from models.boolean import Boolean
from models.creative_work import CreativeWork
from models.integer import Integer
from models.person import Person
from models.text import Text


@dataclass
class Book(CreativeWork):
    abridged: Boolean | None
    bookEdition: Text | None
    bookFormat: BookFormatType | None
    illustrator: Person | None
    isbn: Text | None
    numberOfPages: Integer | None
