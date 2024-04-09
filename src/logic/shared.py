class Shared:
    is_end_of_work = None
    times_finished_work = None

    def __init__(self):
        Shared.is_end_of_work = False
        Shared.times_finished_work = 0
