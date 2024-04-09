import src.tomls.toml_service as toml_service
import src.work.work_service as work_service
import schedule
import time
from src.logic.shared import Shared


config = toml_service.get_config()
shared = Shared()


def main():
    print('Running :D')
    blink_job = schedule.every(config['work']['blink']).minutes.do(work_service.blink_every_20_mins)
    check_email_job = schedule.every(config['work']['check_email']).hours.do(work_service.check_email)
    schedule.every(1).minutes.do(work_service.check_end_of_day)

    while True:
        schedule.run_pending()
        time.sleep(1)
        graceful_shutdown(blink_job, check_email_job)


def graceful_shutdown(blink_job, check_email_job):
    if shared.is_end_of_work:
        schedule.cancel_job(blink_job)
        schedule.cancel_job(check_email_job)
    if shared.is_end_of_work and shared.times_finished_work >= 5:
        exit(0)


if __name__ == "__main__":
    main()
