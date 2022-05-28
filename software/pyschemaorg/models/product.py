# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576275
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.adult_oriented_enumeration import AdultOrientedEnumeration
from models.aggregate_rating import AggregateRating
from models.audience import Audience
from models.boolean import Boolean
from models.brand import Brand
from models.category_code import CategoryCode
from models.country import Country
from models.date import Date
from models.defined_term import DefinedTerm
from models.demand import Demand
from models.distance import Distance
from models.energy_consumption_details import EnergyConsumptionDetails
from models.grant import Grant
from models.image_object import ImageObject
from models.merchant_return_policy import MerchantReturnPolicy
from models.offer import Offer
from models.offer_item_condition import OfferItemCondition
from models.organization import Organization
from models.physical_activity_category import PhysicalActivityCategory
from models.product_group import ProductGroup
from models.product_model import ProductModel
from models.product_return_policy import ProductReturnPolicy
from models.property_value import PropertyValue
from models.quantitative_value import QuantitativeValue
from models.review import Review
from models.service import Service
from models.size_specification import SizeSpecification
from models.text import Text
from models.thing import Thing
from models.url import URL


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
