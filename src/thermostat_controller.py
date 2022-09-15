import RPi.GPIO as GPIO

class ThermostatController:
    room_temperature = 22
    target_temperature = 22

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(21, GPIO.OUT)

    def set_target_temperature(self, target_temperature):
        self.target_temperature = target_temperature

        if self.target_temperature > self.room_temperature:
            self.turn_heating_on()
        else:
            self.turn_heating_off()


    def turn_heating_on(self):
        GPIO.output(21, GPIO.HIGH)
        print("Heating turned on")

    def turn_heating_off(self):
        GPIO.output(21, GPIO.LOW)
        print("Heating turned off")