# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.617989
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .archive_organization import ArchiveOrganization
from .creative_work import CreativeWork
from .place import Place
from .postal_address import PostalAddress
from .text import Text


@dataclass
class ArchiveComponent(CreativeWork):
    holdingArchive: ArchiveOrganization | None
    itemLocation: Place | PostalAddress | Text | None
