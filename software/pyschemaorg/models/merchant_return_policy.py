# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.581290
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .boolean import Boolean
from .country import Country
from .date import Date
from .date_time import DateTime
from .intangible import Intangible
from .integer import Integer
from .merchant_return_enumeration import MerchantReturnEnumeration
from .merchant_return_policy_seasonal_override import MerchantReturnPolicySeasonalOverride
from .monetary_amount import MonetaryAmount
from .number import Number
from .offer_item_condition import OfferItemCondition
from .property_value import PropertyValue
from .refund_type_enumeration import RefundTypeEnumeration
from .return_fees_enumeration import ReturnFeesEnumeration
from .return_label_source_enumeration import ReturnLabelSourceEnumeration
from .return_method_enumeration import ReturnMethodEnumeration
from .text import Text
from .url import URL


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
