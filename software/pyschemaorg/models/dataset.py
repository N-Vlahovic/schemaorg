# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.573490
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.creative_work import CreativeWork
from models.data_catalog import DataCatalog
from models.data_download import DataDownload
from models.date_time import DateTime
from models.property_value import PropertyValue
from models.text import Text
from models.url import URL


@dataclass
class Dataset(CreativeWork):
    catalog: DataCatalog | None
    datasetTimeInterval: DateTime | None
    distribution: DataDownload | None
    includedDataCatalog: DataCatalog | None
    includedInDataCatalog: DataCatalog | None
    issn: Text | None
    measurementTechnique: Text | URL | None
    variableMeasured: PropertyValue | Text | None
    variablesMeasured: PropertyValue | Text | None
