class MyTime:
    minutes = 0
    hours = 0
    days = 0
    weekday = 8

    def __init__(self, txt, weekday=''):
        self.txt_to_time(txt)

        self.weekday = self.update_weekday(weekday)

    def update_weekday(self, weekday):
        wdays = [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday'
        ]
        i = 0
        for day in wdays:
            if (day.upper() == weekday.upper()):
                return i
            i += 1
        i += 1
        return i

    def txt_to_time(self, txt):
        parts = txt.split(':')
        self.hours = int(parts[0])
        minutesPart = parts[1].split(' ')
        self.minutes = int(minutesPart[0])

        if (len(minutesPart) > 1 and minutesPart[1] == 'PM'):
            self.hours += 12

    def min_to_time(self, minutes):
        min_in_day = 24 * 60
        min_in_hour = 60
        self.days = int(minutes / min_in_day)

        if (self.weekday < 8):
            self.weekday = int((self.weekday + self.days ) % 7)

        minutes -= self.days * min_in_day
        self.hours = int(minutes / min_in_hour)
        self.minutes = minutes - (self.hours * min_in_hour)

    def get_string(self):
        amPm = 'AM'
        minDay = self.hours * 60 + self.minutes

        if (minDay > 12 * 60):
            self.hours = self.hours - 12
            amPm = 'PM'

        if (self.hours == 0):
            self.hours = 12

        return f'{self.hours}:{self.minutes:02d} {amPm}{self.get_weekday()}{self.get_days()}'

    def total_minutes(self):
        totalMinutes = self.minutes
        totalMinutes += self.hours * 60
        totalMinutes += self.days * 24 * 60

        return totalMinutes

    def add(self, my_time):
        total_minutes = self.total_minutes()
        total_minutes += my_time.total_minutes()

        self.min_to_time(total_minutes)

    def get_weekday(self):
        wdays = [
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday'
        ]

        if (self.weekday < 8):
            return f', {wdays[self.weekday]}'
        else:
            return ''

    def get_days(self):
        days = ''

        if (self.days > 0):
            days = f' (next day)'

            if (self.days > 1):
                days = f' ({self.days} days later)'

        return days


def add_time(start, duration, weekDay=""):
    startTime = MyTime(start, weekday=weekDay)
    durationTime = MyTime(duration)
    startTime.add(durationTime)
    return startTime.get_string()


# print(add_time("3:00 PM", "3:10"))
# # Returns: 6:10 PM

# print(add_time("11:30 AM", "2:32", "Monday"))
# # Returns: 2:02 PM, Monday

# print(add_time("11:43 AM", "00:20"))
# # Returns: 12:03 PM

# print(add_time("10:10 PM", "3:30"))
# # Returns: 1:40 AM (next day)

# print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "466:02", 'tuesday'))