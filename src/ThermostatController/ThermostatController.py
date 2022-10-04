import RPi.GPIO as GPIO


class ThermostatController:
    def __init__(self):
        print("creating thermostat controller")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)

    def turn_heating_on(self):
        GPIO.output(21, GPIO.HIGH)


    def turn_heating_off(self):
        GPIO.output(21, GPIO.LOW)
