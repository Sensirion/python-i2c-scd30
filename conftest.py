# -*- coding: utf-8 -*-
# (c) Copyright 2021 Sensirion AG, Switzerland

import pytest
from sensirion_shdlc_driver import ShdlcSerialPort, ShdlcConnection
from sensirion_shdlc_sensorbridge import SensorBridgeShdlcDevice


def pytest_addoption(parser):
    """
    Register command line options
    """
    parser.addoption("--serial-port", action="store", type=str)
    parser.addoption("--serial-bitrate", action="store", type=int, default=460800)


def _get_serial_port(config, validate=False):
    """
    Get the serial port to be used for the tests.
    """
    port = config.getoption("--serial-port")
    if (validate is True) and (port is None):
        raise ValueError("Please specify the serial port to be used with "
                         "the '--serial-port' argument.")
    return port


def _get_serial_bitrate(config):
    """
    Get the serial port bitrate to be used for the tests.
    """
    return config.getoption("--serial-bitrate")


def pytest_report_header(config):
    """
    Add extra information to test report header
    """
    lines = [
        "SensorBridge serial port: " + str(_get_serial_port(config)),
        "SensorBridge serial bitrate: " + str(_get_serial_bitrate(config))
    ]
    return '\n'.join(lines)


@pytest.fixture(scope="session")
def bridge(request):
    serial_port = _get_serial_port(request.config, validate=True)
    serial_bitrate = _get_serial_bitrate(request.config)
    with ShdlcSerialPort(serial_port, serial_bitrate) as port:
        dev = SensorBridgeShdlcDevice(ShdlcConnection(port), slave_address=0)
        yield dev
