# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576954
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.tech_article import TechArticle
from models.text import Text


@dataclass
class APIReference(TechArticle):
    assembly: Text | None
    assemblyVersion: Text | None
    executableLibraryName: Text | None
    programmingModel: Text | None
    targetPlatform: Text | None
