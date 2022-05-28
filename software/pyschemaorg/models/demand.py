# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T11:22:09.590309
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from .administrative_area import AdministrativeArea
from .aggregate_offer import AggregateOffer
from .business_entity_type import BusinessEntityType
from .business_function import BusinessFunction
from .creative_work import CreativeWork
from .date import Date
from .date_time import DateTime
from .delivery_method import DeliveryMethod
from .event import Event
from .geo_shape import GeoShape
from .intangible import Intangible
from .item_availability import ItemAvailability
from .loan_or_credit import LoanOrCredit
from .menu_item import MenuItem
from .offer_item_condition import OfferItemCondition
from .organization import Organization
from .payment_method import PaymentMethod
from .person import Person
from .place import Place
from .price_specification import PriceSpecification
from .product import Product
from .quantitative_value import QuantitativeValue
from .service import Service
from .text import Text
from .time import Time
from .trip import Trip
from .type_and_quantity_node import TypeAndQuantityNode
from .warranty_promise import WarrantyPromise


@dataclass
class Demand(Intangible):
    acceptedPaymentMethod: LoanOrCredit | PaymentMethod | None
    advanceBookingRequirement: QuantitativeValue | None
    areaServed: AdministrativeArea | GeoShape | Place | Text | None
    availability: ItemAvailability | None
    availabilityEnds: Date | DateTime | Time | None
    availabilityStarts: Date | DateTime | Time | None
    availableAtOrFrom: Place | None
    availableDeliveryMethod: DeliveryMethod | None
    businessFunction: BusinessFunction | None
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
    includesObject: TypeAndQuantityNode | None
    ineligibleRegion: GeoShape | Place | Text | None
    inventoryLevel: QuantitativeValue | None
    itemCondition: OfferItemCondition | None
    itemOffered: AggregateOffer | CreativeWork | Event | MenuItem | Product | Service | Trip | None
    mpn: Text | None
    priceSpecification: PriceSpecification | None
    seller: Organization | Person | None
    serialNumber: Text | None
    sku: Text | None
    validFrom: Date | DateTime | None
    validThrough: Date | DateTime | None
    warranty: WarrantyPromise | None
