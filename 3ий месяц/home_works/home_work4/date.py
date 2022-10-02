class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month 
        self.day = day
        self.validation()

    def print_date(self):
        print(f'{self.year}/{self.month}{self.day}')

    def validation(self):
        if type(self.year) != int:
            raise DateTimeError("year", self.year, "an integer")
        if type(self.month) != int:
            raise DateTimeError("month", self.month, "an integer")
        if type(self.day) != int:
            raise DateTimeError("day", self.day, "an integer")

        if not self.year in range(0, 9999):
            raise DateTimeError("year", self.year, "between 0 and 9999")
        if not self.month in range(1, 12):
            raise DateTimeError("month", self.month, "between 1 and 12")
        if not self.day in range(1, 31):
            raise DateTimeError("day", self.day, "between 1 and 31")


class DateTime(Date):
    def __init__(self, year, month, day, hours, minutes, seconds):
        super().__init__(year, month, day)
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.validation_date_time()

    def validation_date_time(self):
        super().validation()
        if type(self.hours) != int:
            raise DateTimeError("hours", self.hours, "an integer")
        if type(self.minutes) != int:
            raise DateTimeError("minutes", self.minutes, "an integer")
        if type(self.seconds) != int:
            raise DateTimeError("seconds", self.seconds, "an integer")

        if not self.hours in range(0, 23):
            raise DateTimeError("hours", self.hours, "between 0 and 23")
        if not self.minutes in range(0, 59):
            raise DateTimeError("minutes", self.minutes, "between 0 and 59")
        if not self.seconds in range(0, 59):
            raise DateTimeError("seconds", self.seconds, "between 0 and 59")
    
    def print_datetime(self):
        super().print_date()
        print(f'{self.hours}{self.minutes}{self.seconds}')


class DateTimeError(Exception):
    def __init__(self, date, value, error,*args: object) -> None:
        super().__init__(*args)
        self.date = date
        self.value = value
        self.error = error

    def __str__(self):
        return f'{self.value} for {self.date}. It should be {self.error}'

# date = Date(1958, 8, 23)
# date2 = Date('2002', 20, 4)

# date3 = DateTime(1958, 45, 4, 12, 45, 45)
date4 = DateTime(1958, 5, 4, 12, 75, 45)