# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.586380
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .adult_oriented_enumeration import AdultOrientedEnumeration
from .aggregate_offer import AggregateOffer
from .aggregate_rating import AggregateRating
from .boolean import Boolean
from .business_entity_type import BusinessEntityType
from .business_function import BusinessFunction
from .category_code import CategoryCode
from .creative_work import CreativeWork
from .date import Date
from .date_time import DateTime
from .delivery_method import DeliveryMethod
from .duration import Duration
from .event import Event
from .geo_shape import GeoShape
from .intangible import Intangible
from .item_availability import ItemAvailability
from .loan_or_credit import LoanOrCredit
from .menu_item import MenuItem
from .merchant_return_policy import MerchantReturnPolicy
from .number import Number
from .offer_item_condition import OfferItemCondition
from .offer_shipping_details import OfferShippingDetails
from .organization import Organization
from .payment_method import PaymentMethod
from .person import Person
from .physical_activity_category import PhysicalActivityCategory
from .place import Place
from .price_specification import PriceSpecification
from .product import Product
from .quantitative_value import QuantitativeValue
from .review import Review
from .service import Service
from .text import Text
from .thing import Thing
from .time import Time
from .trip import Trip
from .type_and_quantity_node import TypeAndQuantityNode
from .url import URL
from .warranty_promise import WarrantyPromise


@dataclass
class Offer(Intangible):
    acceptedPaymentMethod: LoanOrCredit | PaymentMethod | None
    addOn: Offer | None
    advanceBookingRequirement: QuantitativeValue | None
    aggregateRating: AggregateRating | None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None
    availability: ItemAvailability | None
    availabilityEnds: Date | DateTime | Time | None
    availabilityStarts: Date | DateTime | Time | None
    availableAtOrFrom: Place | None
    availableDeliveryMethod: DeliveryMethod | None
    businessFunction: BusinessFunction | None
    category: CategoryCode | PhysicalActivityCategory | Text | Thing | URL | None
    deliveryLeadTime: QuantitativeValue | None
    eligibleCustomerType: BusinessEntityType | None
    eligibleDuration: QuantitativeValue | None
    eligibleQuantity: QuantitativeValue | None
    eligibleRegion: GeoShape | Place | Text | None
    eligibleTransactionVolume: PriceSpecification | None
    gtin: Text | None
    gtin12: Text | None
    gtin13: Text | None
    gtin14: Text | None
    gtin8: Text | None
    hasAdultConsideration: AdultOrientedEnumeration | None
    hasMeasurement: QuantitativeValue | None
    hasMerchantReturnPolicy: MerchantReturnPolicy | None
    includesObject: TypeAndQuantityNode | None
    ineligibleRegion: GeoShape | Place | Text | None
    inventoryLevel: QuantitativeValue | None
    isFamilyFriendly: Boolean | None
    itemCondition: OfferItemCondition | None
    itemOffered: AggregateOffer | CreativeWork | Event | MenuItem | Product | Service | Trip | None
    leaseLength: Duration | QuantitativeValue | None
    mpn: Text | None
    offeredBy: Organization | Person | None
    price: Number | Text | None
    priceCurrency: Text | None
    priceSpecification: PriceSpecification | None
    priceValidUntil: Date | None
    review: Review | None
    reviews: Review | None
    seller: Organization | Person | None
    serialNumber: Text | None
    shippingDetails: OfferShippingDetails | None
    sku: Text | None
    validFrom: Date | DateTime | None
    validThrough: Date | DateTime | None
    warranty: WarrantyPromise | None
