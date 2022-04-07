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
from sensirion_i2c_adapter.transfer import execute_transfer
from sensirion_driver_support_types.mixin_access import MixinAccess
from sensirion_i2c_scd30.commands import (ActivateAutoCalibration, ForceRecalibration, GetAltitudeCompensation,
                                          GetAutoCalibrationStatus, GetDataReady, GetForceRecalibrationStatus,
                                          GetMeasurementInterval, GetTemperatureOffset, ReadFirmwareVersion,
                                          ReadMeasurementData, SetAltitudeCompensation, SetMeasurementInterval,
                                          SetTemperatureOffset, SoftReset, StartPeriodicMeasurement,
                                          StopPeriodicMeasurement)


class Scd30DeviceBase:

    def __init__(self, channel):
        self._channel = channel

    @property
    def channel(self):
        return self._channel

    def start_periodic_measurement(self, ambient_pressure):
        """
        Starts continuous measurement of the SCD30 to measure CO₂ concentration, humidity and temperature.
        Measurement data which is not read from the sensor will be overwritten.
        The CO₂ measurement value can be compensated for ambient pressure by feeding the pressure value in mBar to the sensor.
        Setting  the  ambient  pressure  will  overwrite  previous  settings  of  altitude  compensation.
        Setting  the  argument  to  zero  will deactivate the ambient pressure compensation(default ambient pressure = 1013.25 mBar).
        For setting a new ambient pressure when continuous measurement is running the whole command has to be written to SCD30.

        :param ambient_pressure:
            Ambient pressure in millibar.
        """
        transfer = StartPeriodicMeasurement(ambient_pressure)
        return execute_transfer(self._channel, transfer)

    def stop_periodic_measurement(self):
        """Stops the continuous measurement of the SCD30."""
        transfer = StopPeriodicMeasurement()
        return execute_transfer(self._channel, transfer)

    def set_measurement_interval(self, interval):
        """
        Sets the interval used byt he SCD30 sensor to measure in continuous measurement mode. Initial value is 2s.The chosen measurement
        interval is saved in non-volatile memory and thus is not reset to its initial value after power up.

        :param interval:
            Measurement interval in seconds.
        """
        transfer = SetMeasurementInterval(interval)
        return execute_transfer(self._channel, transfer)

    def get_measurement_interval(self):
        """
        Reads out the active measurement interval.

        :return interval:
            Configured measurement interval
        """
        transfer = GetMeasurementInterval()
        return execute_transfer(self._channel, transfer)[0]

    def get_data_ready(self):
        """
        Data ready command is used  to  determine if a measurement can be read from the sensor’s buffer. Whenever there is a measurement
        available from the internal buffer this command returns 1 and 0 otherwise.
        As soon as the measurement has been read by SCD30 the return value changes to 0.

        :return data_ready_flag:
            Data ready flag
        """
        transfer = GetDataReady()
        return execute_transfer(self._channel, transfer)[0]

    def read_measurement_data(self):
        """
        Allows to read new measurement data if data is available.

        :return co2_concentration:

        :return temperature:

        :return humidiy:

        """
        transfer = ReadMeasurementData()
        return execute_transfer(self._channel, transfer)

    def activate_auto_calibration(self, do_activate):
        """
        Continuous automatic self-calibration (ASC) can be (de-)activated with this command. When activated for the first time a period of minimum 7 days
        is needed so that the algorithm can find its initial parameter set for ASC.
        The sensor has to be exposed to fresh air for at least 1 hour every day. Also during that period, the sensor may not be disconnected from the
        power supply. Otherwise the procedure to find calibration parameters is aborted and has to be restarted from the beginning.
        The successfully calculated parameters are stored in non-volatile memory of the SCD30 having the effect that after a restart the previously
        found parameters for ASC are still present.

        :param do_activate:
            Set activate flag.
        """
        transfer = ActivateAutoCalibration(do_activate)
        return execute_transfer(self._channel, transfer)

    def get_auto_calibration_status(self):
        """
        Read out the status of the active self calibration.

        :return is_active:
            Indication if automatic calibration is active
        """
        transfer = GetAutoCalibrationStatus()
        return execute_transfer(self._channel, transfer)[0]

    def force_recalibration(self, co2_ref_concentration):
        """
        Forced recalibration (FRC) is used to compensate for sensor drifts when a reference value of the CO₂ concentration in close proximity to the SCD30 is available.
        For best results, the sensor has to be run in a stable environment in continuous mode at a measurement rate of 2s for at least two minutes before applying the
        FRC commandand sending the reference value. Setting a reference CO₂ concentration by the method described here will always supersede corrections from the
        ASC (see command activate_auto_calibration) and vice-versa.
        The reference CO₂ concentration has to be within the range 400 ppm ≤ cref(CO₂) ≤ 2000 ppm. The FRC method imposes a permanent update of the CO₂ calibration curve
        which persists after repowering the sensor. The most recently used reference value is retained in volatile memory and can be read out with the command sequence
        given below. After repowering the sensor, the command will return the standard reference value of 400 ppm.

        :param co2_ref_concentration:
            New CO2 reference concentration.
        """
        transfer = ForceRecalibration(co2_ref_concentration)
        return execute_transfer(self._channel, transfer)

    def get_force_recalibration_status(self):
        """
        Read out the CO₂ reference concentration.

        :return co2_ref_concentration:
            Currently used CO2 reference concentration.
        """
        transfer = GetForceRecalibrationStatus()
        return execute_transfer(self._channel, transfer)[0]

    def set_temperature_offset(self, temperature_offset):
        """
        The on-board RH/T sensor is influenced by thermal self-heating of SCD30 and other electrical components. Design-in alters the thermal properties of SCD30
        such that temperature and humidity offsets may occur when operating the sensor in end-customer devices.
        Compensation of those effects is achievable by writing the temperature offset found in continuous operation of the device into the sensor. Temperature offset
        value is saved in non-volatile memory. The last set value will be used for temperature offset compensation after repowering

        :param temperature_offset:

        """
        transfer = SetTemperatureOffset(temperature_offset)
        return execute_transfer(self._channel, transfer)

    def get_temperature_offset(self):
        """
        Read out the actual temperature offset. The result can be converted to ℃ by dividing it by 100.

        :return temperature_offset:

        """
        transfer = GetTemperatureOffset()
        return execute_transfer(self._channel, transfer)[0]

    def get_altitude_compensation(self):
        """
        Read out the configured altitude (height in [m] over sea level).

        :return altitude:

        """
        transfer = GetAltitudeCompensation()
        return execute_transfer(self._channel, transfer)[0]

    def set_altitude_compensation(self, altitude):
        """
        Measurements of CO₂ concentration based on the NDIR principle are influenced by altitude. SCD30 offers to compensate deviations due to altitude by using this command.
        Setting altitude is disregarded when an ambient pressure is given to the sensor (see command start_periodic_measurement).
        Altitude value is saved in non-volatile memory. The last set value will be used for altitude compensation after repowering.

        :param altitude:

        """
        transfer = SetAltitudeCompensation(altitude)
        return execute_transfer(self._channel, transfer)

    def read_firmware_version(self):
        """
        Read the version of the current firmware.

        :return major:
            Major version number.
        :return minor:
            Minor version number.
        """
        transfer = ReadFirmwareVersion()
        return execute_transfer(self._channel, transfer)

    def soft_reset(self):
        """
        The SCD30 provides a soft reset mechanism that forces the sensor into the same state as after powering up without the need for removing the power-supply.
        It does so by restarting its system controller. After soft reset the sensor will reload all calibrated data.
        However, it is worth noting that the sensor reloads calibration data prior to every measurement by default. This includes previously set reference values
        from ASC or FRC as well as temperature offset values last setting. The sensor is able to receive the command at any time, regardless of its internal state.
        """
        transfer = SoftReset()
        return execute_transfer(self._channel, transfer)


class Scd30Device(Scd30DeviceBase):
    scd30 = MixinAccess()

    def __init__(self, channel):
        super().__init__(channel)

    def await_data_ready(self):
        """
        Repeatedly call the get_data_ready() until the ready flag is set to 1. A the minimal measuremnt interval is 2s we iterate at most 200 times.
        Note that this is blocking the system for a considerable amount of time!
        """
        data_ready = self.get_data_ready()
        while data_ready == 0:
            time.sleep(0.1)
            data_ready = self.get_data_ready()
        return

    def blocking_read_measurement_data(self):
        """
        This is a convenience method that combines polling the data ready flag and reading out the data.
        Note that this is blocking the system for a considerable amount of time!

        :return co2_concentration:

        :return temperature:

        :return humidiy:

        """
        self.await_data_ready()
        return self.read_measurement_data()
