from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import csv


class TemperatureScheduler:

    def create_schedule(self, target_temperature_service):
        schedule_list = self.read_schedule("TemperatureSchedulerService/resources/schedule.csv")
        scheduler = BackgroundScheduler(daemon=True)

        for cron, target_temperature in schedule_list:
            scheduler.add_job(target_temperature_service.set_target_temperature, CronTrigger.from_crontab(cron),
                              args=[target_temperature])

        scheduler.start()

    def read_schedule(self, filepath):
        with open(filepath, 'r') as file:
            reader = csv.reader(file, delimiter=";")

            schedule = list(((row[0], float(row[1]))
                             for row in reader))

        return schedule

    def delete_schedule(self):
        pass
