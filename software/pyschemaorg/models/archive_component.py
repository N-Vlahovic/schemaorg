# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.595330
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.archive_organization import ArchiveOrganization
from models.creative_work import CreativeWork
from models.place import Place
from models.postal_address import PostalAddress
from models.text import Text


@dataclass
class ArchiveComponent(CreativeWork):
    holdingArchive: ArchiveOrganization | None
    itemLocation: Place | PostalAddress | Text | None
