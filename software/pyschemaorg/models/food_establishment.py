# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.582544
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.local_business import LocalBusiness
from models.menu import Menu
from models.rating import Rating
from models.text import Text
from models.url import URL


@dataclass
class FoodEstablishment(LocalBusiness):
    acceptsReservations: Boolean | Text | URL | None
    hasMenu: Menu | Text | URL | None
    menu: Menu | Text | URL | None
    servesCuisine: Text | None
    starRating: Rating | None
