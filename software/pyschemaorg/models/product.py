# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.585087
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .adult_oriented_enumeration import AdultOrientedEnumeration
from .aggregate_rating import AggregateRating
from .audience import Audience
from .boolean import Boolean
from .brand import Brand
from .category_code import CategoryCode
from .country import Country
from .date import Date
from .defined_term import DefinedTerm
from .demand import Demand
from .distance import Distance
from .energy_consumption_details import EnergyConsumptionDetails
from .grant import Grant
from .image_object import ImageObject
from .merchant_return_policy import MerchantReturnPolicy
from .offer import Offer
from .offer_item_condition import OfferItemCondition
from .organization import Organization
from .physical_activity_category import PhysicalActivityCategory
from .product_group import ProductGroup
from .product_model import ProductModel
from .product_return_policy import ProductReturnPolicy
from .property_value import PropertyValue
from .quantitative_value import QuantitativeValue
from .review import Review
from .service import Service
from .size_specification import SizeSpecification
from .text import Text
from .thing import Thing
from .url import URL


@dataclass
class Product(Thing):
    additionalProperty: PropertyValue | None
    aggregateRating: AggregateRating | None
    audience: Audience | None
    award: Text | None
    awards: Text | None
    brand: Brand | Organization | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    color: Text | None
    countryOfAssembly: Text | None
    countryOfLastProcessing: Text | None
    countryOfOrigin: Country | None
    depth: Distance | QuantitativeValue | None
    funding: Grant | None
    gtin: Text | None
    gtin12: Text | None
    gtin13: Text | None
    gtin14: Text | None
    gtin8: Text | None
    hasAdultConsideration: AdultOrientedEnumeration | None
    hasEnergyConsumptionDetails: EnergyConsumptionDetails | None
    hasMeasurement: QuantitativeValue | None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None
    hasProductReturnPolicy: ProductReturnPolicy | None
    height: Distance | QuantitativeValue | None
    inProductGroupWithID: Text | None
    isAccessoryOrSparePartFor: Product | None
    isConsumableFor: Product | None
    isFamilyFriendly: Boolean | None
    isRelatedTo: Product | Service | None
    isSimilarTo: Product | Service | None
    isVariantOf: ProductGroup | ProductModel | None
    itemCondition: OfferItemCondition | None
    keywords: DefinedTerm | Text | URL | None
    logo: ImageObject | URL | None
    manufacturer: Organization | None
    material: Product | Text | URL | None
    model: ProductModel | Text | None
    mpn: Text | None
    nsn: Text | None
    offers: Demand | Offer | None
    pattern: DefinedTerm | Text | None
    productID: Text | None
    productionDate: Date | None
    purchaseDate: Date | None
    releaseDate: Date | None
    review: Review | None
    reviews: Review | None
    size: DefinedTerm | QuantitativeValue | SizeSpecification | Text | None
    sku: Text | None
    slogan: Text | None
    weight: QuantitativeValue | None
    width: Distance | QuantitativeValue | None
