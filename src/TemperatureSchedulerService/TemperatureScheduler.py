from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger


class TemperatureScheduler:

    def create_schedule(self, target_temperature_service):
        schedule_list = self.read_schedule("schedule.yaml")
        scheduler = BackgroundScheduler(daemon=True)

        for cron, target_temperature in schedule_list:
            scheduler.add_job(target_temperature_service.set_target_temperature, CronTrigger.from_crontab(cron), args=[target_temperature])

        scheduler.start()

    def read_schedule(self, file):
        # TODO: Actually read this from a file
        temp_schedule = [('30 8 * * MON,TUE,FRI', 20),
                         ('30 10 * * MON,TUE,FRI', 17),

                         ('0 7 * * WED,THU', 20),
                         ('0 8 * * WED,THU', 16),

                         ('30 9 * * SAT,SUN', 20),
                         ('30 10 * * SAT,SUN', 16),

                         ('0 0 * * *', 16),
                         ('0 1 * * *', 16)]

        return temp_schedule



    def delete_schedule(self):
        pass