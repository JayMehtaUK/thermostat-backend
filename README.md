# Raspberry Pi Thermostat
The following codebase provides a web interface to interact with a thermostat. The user is able to set a desired temperature and the backend logic will ensure that the desired temperature is met by either turning the heating on or off. 

## Physical Setup
In our setup our Raspberry Pi 3b+ is connected to the following using the GPIO pins:
* [A DHT22 Temperature and Humidity Sensor](https://www.waveshare.com/wiki/DHT22_Temperature-Humidity_Sensor)
* [A Salus ERT20TX Thermostat](https://salus-controls.com/files/ERT20TX-Ver002.pdf) via a [5V relay](https://www.amazon.co.uk/gp/product/B01H2D2RI0/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)

The Salus thermostat is connected to the boiler over a wireless signal. However, the thermostat itself lacks features of a smart thermostat. The back of the Salus thermostat has various pins. By default, when none of the pins are bridged (connected to each other) the thermostat is in heating mode. If we bridge the cooling pins together the thermostat will switch to cooling mode. As we are not connected to a cooling system, we can exploit this and switch to cooling mode in order to turn the heating off. 

In order to bridge the cooling pins together we are using a [relay](https://en.wikipedia.org/wiki/Relay) in order to programmatically bridge the cooling pins when we want to turn the heating off. Below is a diagram showing the setup:

```mermaid
graph LR;
    RaspberryPi --> Relay;
    RaspberryPi --> DHT22;
    Relay --> Thermostat;
```

## High Level Overview
### Room Temperature Service
The room temperature service provides functionality to continuously poll the DHT22 device to get an up to date reading for the current temperature and humidity.

### Target Temperature Service
The target temperature service provides functionality to a background service to continuously check if the current room temperature has reached the target temperature.

If the target temperature has been met the heating is turned off. Otherwise, the heating is turned on (or stays on).

### Thermostat Controller
The thermostat controller provides an interface between the Raspberry Pi and the Relay that will bridge the cooling pins on the thermostat. We have abstracted this away and from the controllers point of view it is either turing the thermostat on or off. 

### Temperature Scheduler Service
> 📝 This is currently a work in progress

The temperature scheduler service allows you to create custom schedules to turn the heating on or off using a list of CRON expressions. 

Currently, these have been hardcoded in the service. However, at some point we can modify this to read in the schedule from an external source (such as a file or database). We can then provide another web page to configure the schedule and update it when required.
