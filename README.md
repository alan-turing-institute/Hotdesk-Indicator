# Hotdesk-Indicator
Displaying the status of a hotdesk using a raspberrypi and the Inky pHAT

## Installation

First ensure the SPI interface is enabled. This can be achieved with
`raspi-config`, the Raspberry Pi Configuration gui tool, or

```
$ sudo sed -i 's/^#dtparam=spi=on/dtparam=spi=on/g' /boot/config.txt
```

Next clone the repository

```
$ git clone https://github.com/alan-turing-institute/Hotdesk-Indicator.git
```

and install using pip

```
$ sudo apt install python3-pip
$ cd Hotdesk-Indicator
$ pip3 install .
```

A summary of the usage commands can be seen with

```
$ hotdesk-set -h
```

and

```
$ hotdesk-get -h
```
