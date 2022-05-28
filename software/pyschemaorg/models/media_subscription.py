# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.587815
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .intangible import Intangible
from .offer import Offer
from .organization import Organization


@dataclass
class MediaSubscription(Intangible):
    authenticator: Organization | None
    expectsAcceptanceOf: Offer | None
