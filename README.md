# Python libraries for Waveshare e-paper series
Python libraries for Waveshare e-paper series
# About
This repo was created to provide a convenient way to install e-paper library for Raspberry Pi.
The original code is provided by [Waveshare GitHub](https://github.com/soonuse/epd-library-python).
## Raspberry Pi GPIO Pin map 
    +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
    | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
    +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
    |     |     |    3.3v |      |   |  1 || 2  |   |      | 5v      |     |     |
    |   2 |   8 |   SDA.1 |   IN | 1 |  3 || 4  |   |      | 5v      |     |     |
    |   3 |   9 |   SCL.1 |   IN | 1 |  5 || 6  |   |      | 0v      |     |     |
    |   4 |   7 | GPIO. 7 |   IN | 1 |  7 || 8  | 1 | ALT5 | TxD     | 15  | 14  |
    |     |     |      0v |      |   |  9 || 10 | 1 | ALT5 | RxD     | 16  | 15  |
    |  17 |   0 | GPIO. 0 |   IN | 0 | 11 || 12 | 0 | IN   | GPIO. 1 | 1   | 18  |
    |  27 |   2 | GPIO. 2 |   IN | 0 | 13 || 14 |   |      | 0v      |     |     |
    |  22 |   3 | GPIO. 3 |   IN | 0 | 15 || 16 | 0 | IN   | GPIO. 4 | 4   | 23  |
    |     |     |    3.3v |      |   | 17 || 18 | 0 | IN   | GPIO. 5 | 5   | 24  |
    |  10 |  12 |    MOSI | ALT0 | 0 | 19 || 20 |   |      | 0v      |     |     |
    |   9 |  13 |    MISO | ALT0 | 0 | 21 || 22 | 0 | IN   | GPIO. 6 | 6   | 25  |
    |  11 |  14 |    SCLK | ALT0 | 0 | 23 || 24 | 1 | OUT  | CE0     | 10  | 8   |
    |     |     |      0v |      |   | 25 || 26 | 1 | OUT  | CE1     | 11  | 7   |
    |   0 |  30 |   SDA.0 |   IN | 1 | 27 || 28 | 1 | IN   | SCL.0   | 31  | 1   |
    |   5 |  21 | GPIO.21 |   IN | 1 | 29 || 30 |   |      | 0v      |     |     |
    |   6 |  22 | GPIO.22 |   IN | 1 | 31 || 32 | 0 | IN   | GPIO.26 | 26  | 12  |
    |  13 |  23 | GPIO.23 |   IN | 0 | 33 || 34 |   |      | 0v      |     |     |
    |  19 |  24 | GPIO.24 |  OUT | 1 | 35 || 36 | 1 | OUT  | GPIO.27 | 27  | 16  |
    |  26 |  25 | GPIO.25 |   IN | 0 | 37 || 38 | 0 | IN   | GPIO.28 | 28  | 20  |
    |     |     |      0v |      |   | 39 || 40 | 0 | IN   | GPIO.29 | 29  | 21  |
    +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
    | BCM | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | BCM |
    +-----+-----+---------+------+---+---Pi 3---+---+------+---------+-----+-----+
## Hardware connection (OLED => Raspberry Pi)
  * VCC    ->    3.3
  * GND    ->    GND
  * DIN    ->    MOSI
  * CLK    ->    SCLK
  * CS     ->    24 (Physical, BCM: CE0, 8)
  * D/C    ->    22 (Physical, BCM: 25)
  * RES    ->    11 (Physical, BCM: 17)
  * BUSY   ->    18 (Physical, BCM: 24)
## How to use
1.  install libraries required libraries and demos via 
    <pre>pip install epd-library</pre>
2.  run the demo with: 
  * 1.54inch e-paper
    <pre>epd1in54</pre>
  * 1.54inch e-paper b
    <pre>epd1in54b</pre>
  * 1.54inch e-paper c
    <pre>epd1in54c</pre>
  * 2.13inch e-paper
    <pre>epd2in13</pre>
  * 2.13inch e-paper b
    <pre>epd2in13b</pre>
  * 2.7inch e-paper
    <pre>epd2in7</pre>
  * 2.7inch e-paper b
    <pre>epd2in7b</pre>
  * 2.9inch e-paper
    <pre>epd2in9</pre>
  * 2.9inch e-paper b
    <pre>epd2in9b</pre>
  * 4.2inch e-paper
    <pre>epd4in2</pre>
  * 4.2inch e-paper b
    <pre>epd4in2b</pre>
  * 7.5inch e-paper
    <pre>epd7in5</pre>
  * 7.5inch e-paper b
    <pre>epd7in5b</pre>
## Supported models

Standard Raspberry Pi header on module, allowed to be attached onto Pi directly, compatible with Raspberry Pi 40PIN GPIO extension header

* GDEP015OC1 - [e-paper library for Raspberry Pi](https://www.waveshare.com/wiki/1.54inch_e-Paper_Module) - epd1in54
* GDEW0154Z04 - [e-paper library for Raspberry Pi](https://www.waveshare.com/wiki/1.54inch_e-Paper_Module_(B)) - epd1in54b
* [1.54inch e-Paper Module (C)](https://www.waveshare.com/wiki/1.54inch_e-Paper_Module_(C)) - epd1in54c
* GDEM0213E26LT - [2.13" e-paper library for Raspberry Pi](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT) - epd2in13
* GDEW0213Z16 - [2.13" e-paper display (B) library for Raspberry Pi](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_(B)) - epd2in13b
* GDEW027W3 - [2.7" e-paper library for Raspberry Pi](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT) - epd2in7
* GDEW027C44 - [2.7" e-paper display (B) library for Raspberry Pi](https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT_(B)) - epd2in7b
* GDEH029A1 - [2.9" e-paper display library for Raspberry Pi](https://www.waveshare.com/wiki/2.9inch_e-Paper_Module) - epd2in9
* GDEW029Z10 - [2.9" e-paper display (B) library for Raspberry Pi](https://www.waveshare.com/wiki/2.9inch_e-Paper_Module_(B)) - epd2in9b
* GDEW042T2 - [4.2" e-paper display library for Raspberry Pi](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module) - epd4in2
* GDEW042Z15 - [4.2" e-paper display (B) library for Raspberry Pi](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module_(B)) - epd4in2b
* GDEW075T8 - [7.5" e-paper display library for Raspberry Pi](https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT)
* GDEW075Z09 - [7.5" e-paper display (B) library for Raspberry Pi](https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT_(B))

![e-paper display](http://www.waveshare.com/img/devkit/general/e-Paper-Modules-CMP.jpg)
# Interfaces
| Name | Description                                                   |
|------|---------------------------------------------------------------|
| VCC  | 3.3V                                                          |
| GND  | GND                                                           |
| DIN  | SPI MOSI                                                      |
| CLK  | SPI SCK                                                       |
| CS   | SPI chip select (Low active)                                  |
| DC   | Data/Command control pin (High for data, and low for command) |
| RST  | External reset pin (Low for reset)                            |
| BUSY | Busy state output pin (Low for busy)                          |



