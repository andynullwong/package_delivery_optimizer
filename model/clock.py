from datetime import datetime, timedelta


def string_to_timestamp(string):
    return datetime.strptime(string, "%Y-%m-%d %H:%M:%S")


class Clock:
    def __init__(self):
        self.time = datetime(2020, 1, 1, 8, 0)  # 2020, January 1, 8:00

    def get_time(self):
        return self.time

    def add_time(self, hours, minutes=0):
        self.time += timedelta(hours=hours, minutes=minutes)

    def tick(self):
        self.time += timedelta(hours=0, minutes=1)


# Initialize Global Clock as single source of time management
clock = Clock()
