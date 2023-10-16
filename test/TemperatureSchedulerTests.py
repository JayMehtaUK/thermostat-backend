import unittest
from src.TemperatureSchedulerService.TemperatureScheduler import TemperatureScheduler


class TemperatureSchedulerTests(unittest.TestCase):
    def setUp(self):
        self.temperature_scheduler = TemperatureScheduler()

    def test_read_schedule_from_file(self):
        expected_schedule = [
            ('0 8 * * MON,TUE,FRI', 18.0),
            ('0 11 * * MON,TUE,FRI', 14.0),
            ('0 6 * * WED,THU', 17.0)
        ]

        schedule = self.temperature_scheduler.read_schedule('TestData/test_schedule.csv')
        self.assertEqual(schedule, expected_schedule)

