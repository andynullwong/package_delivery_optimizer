from datetime import datetime, timedelta


class Clock:
    def __init__(self):
        self.time = datetime(2020, 1, 1, 8, 0)  # 2020, January 1, 8:00

    def get_time(self):
        return self.time

    def add_time(self, hours, minutes=0):
        self.time += timedelta(hours=hours, minutes=minutes)

    def tick(self):
        self.time += timedelta(hours=0, minutes=1)