# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.596511
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .local_business import LocalBusiness
from .menu import Menu
from .rating import Rating
from .text import Text
from .url import URL


@dataclass
class FoodEstablishment(LocalBusiness):
    acceptsReservations: Boolean | Text | URL | None
    hasMenu: Menu | Text | URL | None
    menu: Menu | Text | URL | None
    servesCuisine: Text | None
    starRating: Rating | None
