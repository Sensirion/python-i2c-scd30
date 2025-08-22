# Python I2C Driver for Sensirion SCD30

This repository contains the Python driver to communicate with a Sensirion SCD30 sensor over I2C.

<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-scd30/master/images/sensor_scd30_image.jpg"
    width="300px" alt="SCD30 picture">


Click [here](https://sensirion.com/products/catalog/SCD30/) to learn more about the Sensirion SCD30 sensor.



The default I²C address of [SCD30](https://sensirion.com/products/catalog/SCD30/) is **0x61**.



## Connect the sensor

You can connect your sensor over a [SEK-SensorBridge](https://developer.sensirion.com/product-support/sek-sensorbridge/).
For special setups you find the sensor pinout in the section below.

<details><summary>Sensor pinout</summary>
<p>
<img src="https://raw.githubusercontent.com/Sensirion/python-i2c-scd30/master/images/scd30_pinout.jpg"
     width="300px" alt="sensor wiring picture">

| *Pin* | *Cable Color* | *Name* | *Description*  | *Comments* |
|-------|---------------|:------:|----------------|------------|
| 1 | red | VDD | Supply Voltage | 3.3V to 5.5V
| 2 | black | GND | Ground |
| 3 | yellow | SCL | I2C: Serial clock input |
| 4 | green | SDA | I2C: Serial data input / output |
| 5 |  | RDY |  | High when data is available - do not connect
| 6 |  | PWM |  | do not connect
| 7 | blue | SEL | Interface select | Pull to ground or floating for I2C


</p>
</details>


## Documentation & Quickstart

See the [documentation page](https://sensirion.github.io/python-i2c-scd30) for an API description and a
[quickstart](https://sensirion.github.io/python-i2c-scd30/execute-measurements.html) example.


## Contributing

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

## License

See [LICENSE](LICENSE).