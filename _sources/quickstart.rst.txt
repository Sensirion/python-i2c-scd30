Quick Start
===========

Execute measurements with SensorBridge
---------------------------------------

Installing the SensorBridge Driver
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The driver for the `Sensirion SEK-SensorBridge`_ can be installed with

.. sourcecode:: bash

    pip install sensirion-shdlc-sensorbridge

.. _Sensirion SEK-SensorBridge: https://developer.sensirion.com/sensirion-products/sek-sensorbridge/

Example script
~~~~~~~~~~~~~~

The following script shows how to use this driver on a Windows system using the `Sensirion SEK-SensorBridge`_ to
execute a simple measurement.

.. literalinclude:: ../examples/example_sensorbridge_scd30.py
    :language: python

Execute measurements using internal Linux I²C driver
----------------------------------------------------

On Linux systems it is furthermore possible to use the Linux user space I²C driver directly.
How this can be done (e.g. for a sensor attached to the Raspberry Pi I²C port 1) is shown in the following script.

.. literalinclude:: ../examples/example_linux_scd30.py
    :language: python
