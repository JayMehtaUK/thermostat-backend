from ThermostatController.ThermostatController import ThermostatController
from RoomTemperatureService.RoomTemperature import RoomTemperature


class TargetTemperature:
    def __init__(self, room_temperature_service: RoomTemperature):
        self.target_temperature = 16
        self.room_temperature_service = room_temperature_service
        self.thermostat_controller = ThermostatController()
        # Set the initial state so the logic for reaching target temp can work
        self.thermostat_controller.turn_heating_off()
        self.is_heating_on = False

        print("Target Temperature Service Created")

    def reach_target_temperature(self):
        room_temperature = self.room_temperature_service.get_room_temperature()

        if self.target_temperature > room_temperature:
            if not self.is_heating_on:
                print(f'Heating turning on. Room Temp: {room_temperature} | Desired Temp: {self.target_temperature}')
                self.thermostat_controller.turn_heating_on()
                self.is_heating_on = True
        else:
            if self.is_heating_on:
                print(f'Heating turning off. Room Temp: {room_temperature} | Desired Temp: {self.target_temperature}')
                self.thermostat_controller.turn_heating_off()
                self.is_heating_on = False
