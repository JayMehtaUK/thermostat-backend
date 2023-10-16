from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import csv
import config


class TemperatureScheduler:
    scheduler = BackgroundScheduler(daemon=True)

    def __init__(self, target_temperature_service):
        self.target_temperature_service = target_temperature_service

    def create_schedule(self):
        self.update_schedule()
        self.scheduler.start()

    def update_schedule(self):
        self.scheduler.remove_all_jobs()
        schedule_list = self.read_schedule(config.schedule_path)

        for cron, target_temperature in schedule_list:
            self.scheduler.add_job(self.target_temperature_service.set_target_temperature,
                                   CronTrigger.from_crontab(cron),
                                   args=[target_temperature])

    def read_schedule(self, filepath):
        with open(filepath, 'r') as file:
            reader = csv.reader(file, delimiter=";")

            schedule = list(((row[0], float(row[1]))
                             for row in reader))

        return schedule

    def read_schedule_raw(self, filepath):
        with open(filepath, 'r') as file:
            schedule = file.read()

        return schedule

    def save_schedule(self, filepath, schedule):
        with open(filepath, 'w') as file:
            file.write(schedule)
