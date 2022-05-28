# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.601872
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.medical_audience import MedicalAudience
from models.medical_audience_type import MedicalAudienceType
from models.text import Text
from models.web_page import WebPage


@dataclass
class MedicalWebPage(WebPage):
    aspect: Text | None
    medicalAudience: MedicalAudience | MedicalAudienceType | None
