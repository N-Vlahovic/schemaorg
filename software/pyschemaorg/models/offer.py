# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.576889
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.adult_oriented_enumeration import AdultOrientedEnumeration
from models.aggregate_offer import AggregateOffer
from models.aggregate_rating import AggregateRating
from models.boolean import Boolean
from models.business_entity_type import BusinessEntityType
from models.business_function import BusinessFunction
from models.category_code import CategoryCode
from models.creative_work import CreativeWork
from models.date import Date
from models.date_time import DateTime
from models.delivery_method import DeliveryMethod
from models.duration import Duration
from models.event import Event
from models.geo_shape import GeoShape
from models.intangible import Intangible
from models.item_availability import ItemAvailability
from models.loan_or_credit import LoanOrCredit
from models.menu_item import MenuItem
from models.merchant_return_policy import MerchantReturnPolicy
from models.number import Number
from models.offer_item_condition import OfferItemCondition
from models.offer_shipping_details import OfferShippingDetails
from models.organization import Organization
from models.payment_method import PaymentMethod
from models.person import Person
from models.physical_activity_category import PhysicalActivityCategory
from models.place import Place
from models.price_specification import PriceSpecification
from models.product import Product
from models.quantitative_value import QuantitativeValue
from models.review import Review
from models.service import Service
from models.text import Text
from models.thing import Thing
from models.time import Time
from models.trip import Trip
from models.type_and_quantity_node import TypeAndQuantityNode
from models.url import URL
from models.warranty_promise import WarrantyPromise


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
