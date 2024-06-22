from datetime import datetime

class SuperDate(datetime):

    def __init__(self, y, m, d, time):
        self.y = y
        self.m = m
        self.d = d
        self.time = time

    def get_season(self):
        if self.m == 12 or self.m == 1 or self.m == 2:
            season = 'Winter'
        elif self.m == 3 or self.m == 4 or self.m == 5:
            season = 'Spring'
        elif self.m == 6 or self.m == 7 or self.m == 8:
            season = 'Summer'
        else:
            season = 'Autumn'
        return season

    def get_time_of_day(self):
        if self.time >= 6 and self.time < 12:
            times_of_day = 'Morning'
        elif self.time >= 12 and self.time < 18:
            times_of_day = 'Day'
        elif self.time >= 18 and self.time < 0:
            times_of_day = 'Evening'
        else:
            times_of_day = 'Night'
        return times_of_day

a = SuperDate(2024, 6, 22, 5)
print(a.get_season())
print(a.get_time_of_day())