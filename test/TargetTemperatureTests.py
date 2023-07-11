import unittest
from RoomTemperatureService.RoomTemperature import RoomTemperature
from TargetTemperatureService.TargetTemperature import TargetTemperature


class TargetTemperatureTests(unittest.TestCase):
    def setUp(self) -> None:
        room_temperature_service = RoomTemperature()
        room_temperature_service.room_temperature = 15
        self.target_temperature_service = TargetTemperature(room_temperature_service)

    def test_reach_target_temperature_turns_heating_on(self):
        self.target_temperature_service.target_temperature = 20
        self.target_temperature_service.reach_target_temperature()
        self.assertTrue(self.target_temperature_service.is_heating_on)

    def test_reach_target_temperature_turns_heating_off(self):
        self.target_temperature_service.target_temperature = 10
        self.target_temperature_service.reach_target_temperature()
        self.assertFalse(self.target_temperature_service.is_heating_on)
