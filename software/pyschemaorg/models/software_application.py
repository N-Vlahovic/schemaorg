# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.581008
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .data_feed import DataFeed
from .image_object import ImageObject
from .text import Text
from .url import URL


@dataclass
class SoftwareApplication(CreativeWork):
    applicationCategory: Text | URL | None
    applicationSubCategory: Text | URL | None
    applicationSuite: Text | None
    availableOnDevice: Text | None
    countriesNotSupported: Text | None
    countriesSupported: Text | None
    device: Text | None
    downloadUrl: URL | None
    featureList: Text | URL | None
    fileSize: Text | None
    installUrl: URL | None
    memoryRequirements: Text | URL | None
    operatingSystem: Text | None
    permissions: Text | None
    processorRequirements: Text | None
    releaseNotes: Text | URL | None
    requirements: Text | URL | None
    screenshot: ImageObject | URL | None
    softwareAddOn: SoftwareApplication | None
    softwareHelp: CreativeWork | None
    softwareRequirements: Text | URL | None
    softwareVersion: Text | None
    storageRequirements: Text | URL | None
    supportingData: DataFeed | None
