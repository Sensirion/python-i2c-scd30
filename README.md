# Python I2C Driver for Sensirion SCD30

This repository contains the Python driver to communicate with the Sensirion
SCD30 sensor over I2C. 

<center><img src="images/sensor_scd30_image.jpg" width="300px"></center>

Click [here](https://sensirion.com/products/catalog/SCD30/) to learn more about the Sensirion SCD30 sensor.



The default I²C address of [SCD30](https://sensirion.com/products/catalog/SCD30/) is **0x61**.



## Usage

See user manual at
[https://sensirion.github.io](https://sensirion.github.io/python-i2c-scd30).

#### Detaild sensor pinout

<img src="images/scd30_pinout.jpg" width="300px">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | red |VDD | Supply Voltage | 3.3 to 5.5V
| 2 | black |GND | Ground | 
| 3 | yellow |SCL | I2C: Serial clock input | 
| 4 | green |SDA | I2C: Serial data input / output | 
| 5 |  |RDY | High when data is available | do not connect
| 6 |  |PWM |  | do not connect
| 7 | blue |SEL | Interface select | Pull to ground or floating for I2c

## Development

We develop and test this driver using our company internal tools (version
control, continuous integration, code review etc.) and automatically
synchronize the `master` branch with GitHub. But this doesn't mean that we
don't respond to issues or don't accept pull requests on GitHub. In fact,
you're very welcome to open issues or create pull requests :)

### Check coding style

The coding style can be checked with [`flake8`](http://flake8.pycqa.org/):

```bash
pip install -e .[test]  # Install requirements
flake8                  # Run style check
```

In addition, we check the formatting of files with
[`editorconfig-checker`](https://editorconfig-checker.github.io/):

```bash
pip install editorconfig-checker==2.0.3   # Install requirements
editorconfig-checker                      # Run check
```

### Run tests

Unit tests can be run with [`pytest`](https://pytest.org/):

```bash
pip install -e .[test]                       # Install requirements
pytest -m "not needs_device"                 # Run tests without hardware
pytest                                       # Run all tests
pytest -m "needs_device"  # Run all tests for SPS6x

```

The tests with the marker `needs_device` have following requirements:

- The SCD30 sensor must be connected to a
  [SensorBridge](https://www.sensirion.com/sensorbridge/) on port 1.
- Pass the serial port where the SensorBridge is connected with
  `--serial-port`, e.g. `pytest --serial-port=COM7`
- The SensorBridge must have default settings (baudrate 460800, address 0)


### Build documentation

The documentation can be built with [Sphinx](http://www.sphinx-doc.org/):

```bash
python setup.py install                        # Install package
pip install -r docs/requirements.txt           # Install requirements
sphinx-versioning build docs docs/_build/html  # Build documentation
```

## License

See [LICENSE](LICENSE).
