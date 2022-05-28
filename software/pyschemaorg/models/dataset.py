# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.579934
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .creative_work import CreativeWork
from .data_catalog import DataCatalog
from .data_download import DataDownload
from .date_time import DateTime
from .property_value import PropertyValue
from .text import Text
from .url import URL


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
