#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2022 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:    sensirion-driver-generator 0.9.0
# Product:      scd30
# Version:      None
#

import time
from sensirion_i2c_driver import I2cConnection, CrcCalculator
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import (SensorBridgePort,
                                          SensorBridgeShdlcDevice,
                                          SensorBridgeI2cProxy)
from sensirion_i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_scd30.device import Scd30Device
with ShdlcSerialPort(port='COM1', baudrate=460800) as port:
    bridge = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
    bridge.set_i2c_frequency(SensorBridgePort.ONE, frequency=100e3)
    bridge.set_supply_voltage(SensorBridgePort.ONE, voltage=3.3)
    bridge.switch_supply_on(SensorBridgePort.ONE)
    i2c_transceiver = SensorBridgeI2cProxy(bridge, port=SensorBridgePort.ONE)
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x61,
                         crc=CrcCalculator(8, 0x31, 0xff, 0x0))
    sensor = Scd30Device(channel)
    try:
        sensor.stop_periodic_measurement()
        sensor.soft_reset()
        time.sleep(2.0)
    except BaseException:
        ...

    (major, minor) = sensor.read_firmware_version()
    print(f"firmware version major: {major}; minor: {minor}; ")
    sensor.start_periodic_measurement(0)
    for i in range(30):
        try:
            time.sleep(1.5)
            (co2_concentration, temperature, humidity
             ) = sensor.blocking_read_measurement_data()
            print(f"co2_concentration: {co2_concentration}; temperature: {temperature}; humidity: {humidity}; ")
        except BaseException:
            continue
    sensor.stop_periodic_measurement()