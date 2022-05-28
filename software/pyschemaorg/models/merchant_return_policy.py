# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.574213
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.boolean import Boolean
from models.country import Country
from models.date import Date
from models.date_time import DateTime
from models.intangible import Intangible
from models.integer import Integer
from models.merchant_return_enumeration import MerchantReturnEnumeration
from models.merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
from models.monetary_amount import MonetaryAmount
from models.number import Number
from models.offer_item_condition import OfferItemCondition
from models.property_value import PropertyValue
from models.refund_type_enumeration import RefundTypeEnumeration
from models.return_fees_enumeration import ReturnFeesEnumeration
from models.return_label_source_enumeration import ReturnLabelSourceEnumeration
from models.return_method_enumeration import ReturnMethodEnumeration
from models.text import Text
from models.url import URL


@dataclass
class MerchantReturnPolicy(Intangible):
    additionalProperty: PropertyValue | None
    applicableCountry: Country | Text | None
    customerRemorseReturnFees: ReturnFeesEnumeration | None
    customerRemorseReturnLabelSource: ReturnLabelSourceEnumeration | None
    customerRemorseReturnShippingFeesAmount: MonetaryAmount | None
    inStoreReturnsOffered: Boolean | None
    itemCondition: OfferItemCondition | None
    itemDefectReturnFees: ReturnFeesEnumeration | None
    itemDefectReturnLabelSource: ReturnLabelSourceEnumeration | None
    itemDefectReturnShippingFeesAmount: MonetaryAmount | None
    merchantReturnDays: Date | DateTime | Integer | None
    merchantReturnLink: URL | None
    refundType: RefundTypeEnumeration | None
    restockingFee: MonetaryAmount | Number | None
    returnFees: ReturnFeesEnumeration | None
    returnLabelSource: ReturnLabelSourceEnumeration | None
    returnMethod: ReturnMethodEnumeration | None
    returnPolicyCategory: MerchantReturnEnumeration | None
    returnPolicyCountry: Country | Text | None
    returnPolicySeasonalOverride: MerchantReturnPolicySeasonalOverride | None
    returnShippingFeesAmount: MonetaryAmount | None
