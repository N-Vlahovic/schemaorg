# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.578810
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.administrative_area import AdministrativeArea
from models.aggregate_offer import AggregateOffer
from models.business_entity_type import BusinessEntityType
from models.business_function import BusinessFunction
from models.creative_work import CreativeWork
from models.date import Date
from models.date_time import DateTime
from models.delivery_method import DeliveryMethod
from models.event import Event
from models.geo_shape import GeoShape
from models.intangible import Intangible
from models.item_availability import ItemAvailability
from models.loan_or_credit import LoanOrCredit
from models.menu_item import MenuItem
from models.offer_item_condition import OfferItemCondition
from models.organization import Organization
from models.payment_method import PaymentMethod
from models.person import Person
from models.place import Place
from models.price_specification import PriceSpecification
from models.product import Product
from models.quantitative_value import QuantitativeValue
from models.service import Service
from models.text import Text
from models.time import Time
from models.trip import Trip
from models.type_and_quantity_node import TypeAndQuantityNode
from models.warranty_promise import WarrantyPromise


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
