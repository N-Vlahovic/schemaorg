# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574081
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.data_feed import DataFeed
from models.image_object import ImageObject
from models.text import Text
from models.url import URL


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
