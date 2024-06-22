from datetime import datetime

class SuperDate(datetime):


    def get_season(self):
        if self.month == 12 or self.month == 1 or self.month == 2:
            season = 'Winter'
        elif self.month == 3 or self.month == 4 or self.month == 5:
            season = 'Spring'
        elif self.month == 6 or self.month == 7 or self.month == 8:
            season = 'Summer'
        else:
            season = 'Autumn'
        return season


    def get_time_of_day(self):
        if self.hour >= 6 and self.hour < 12:
            times_of_day = 'Morning'
        elif self.hour >= 12 and self.hour < 18:
            times_of_day = 'Day'
        elif self.hour >= 18 and self.hour < 0:
            times_of_day = 'Evening'
        else:
            times_of_day = 'Night'
        return times_of_day


a = SuperDate(2024, 6, 22, 5)
print(a.get_season())
print(a.get_time_of_day())