import time
from ..tomls import toml_service
from ..sound import sound_service
from ..logic import shared


config = toml_service.get_config()


def check_end_of_day():
    yr, month, day, hr, minute = map(int, time.strftime("%Y %m %d %H %M").split())
    if hr == config['work']['day_end']:
        sound_service.play_sound(config['sound']['day_end'])
        shared.Shared.is_end_of_work = True
        shared.Shared.times_finished_work += 1
        print('Day finish')


def check_email():
    print('Remember to check your email')
    yr, month, day, hr, minute = map(int, time.strftime("%Y %m %d %H %M").split())
    if hr == config['work']['check_email']:
        sound_service.play_sound(config['sound']['check_email'])


def blink_every_20_mins():
    print('Remember to blink')
    sound_service.play_sound(config['sound']['blink'])
