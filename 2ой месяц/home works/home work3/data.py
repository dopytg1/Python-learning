from datetime import date

name = input("Enter your name:")
lastName = input("Enter your last name:")
birthday = int(input("When were you born?:"))
country = input("Where are you from?:")
currentYear = int(date.today().year) # current year from module datetime

def count_birthday(year = 2022) -> int:
    return year - birthday


print("Hello %s %s.You are %s years old. You are living in %s" %(name.capitalize(), lastName.capitalize(), count_birthday(currentYear), country.capitalize()))