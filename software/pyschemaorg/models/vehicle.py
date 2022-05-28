# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Auto-generated on 2022-05-28T12:00:23.575962
# For more info concerning Schema.org c.f. https://schema.org/
# For more info concerning this script c.f. nikolai@nexup.com
from __future__ import annotations
from dataclasses import dataclass

from models.car_usage_type import CarUsageType
from models.date import Date
from models.drive_wheel_configuration_value import DriveWheelConfigurationValue
from models.engine_specification import EngineSpecification
from models.number import Number
from models.product import Product
from models.qualitative_value import QualitativeValue
from models.quantitative_value import QuantitativeValue
from models.steering_position_value import SteeringPositionValue
from models.text import Text
from models.url import URL


@dataclass
class Vehicle(Product):
    accelerationTime: QuantitativeValue | None
    bodyType: QualitativeValue | Text | URL | None
    callSign: Text | None
    cargoVolume: QuantitativeValue | None
    dateVehicleFirstRegistered: Date | None
    driveWheelConfiguration: DriveWheelConfigurationValue | Text | None
    emissionsCO2: Number | None
    fuelCapacity: QuantitativeValue | None
    fuelConsumption: QuantitativeValue | None
    fuelEfficiency: QuantitativeValue | None
    fuelType: QualitativeValue | Text | URL | None
    knownVehicleDamages: Text | None
    meetsEmissionStandard: QualitativeValue | Text | URL | None
    mileageFromOdometer: QuantitativeValue | None
    modelDate: Date | None
    numberOfAirbags: Number | Text | None
    numberOfAxles: Number | QuantitativeValue | None
    numberOfDoors: Number | QuantitativeValue | None
    numberOfForwardGears: Number | QuantitativeValue | None
    numberOfPreviousOwners: Number | QuantitativeValue | None
    payload: QuantitativeValue | None
    productionDate: Date | None
    purchaseDate: Date | None
    seatingCapacity: Number | QuantitativeValue | None
    speed: QuantitativeValue | None
    steeringPosition: SteeringPositionValue | None
    stupidProperty: QuantitativeValue | None
    tongueWeight: QuantitativeValue | None
    trailerWeight: QuantitativeValue | None
    vehicleConfiguration: Text | None
    vehicleEngine: EngineSpecification | None
    vehicleIdentificationNumber: Text | None
    vehicleInteriorColor: Text | None
    vehicleInteriorType: Text | None
    vehicleModelDate: Date | None
    vehicleSeatingCapacity: Number | QuantitativeValue | None
    vehicleSpecialUsage: CarUsageType | Text | None
    vehicleTransmission: QualitativeValue | Text | URL | None
    weightTotal: QuantitativeValue | None
    wheelbase: QuantitativeValue | None
