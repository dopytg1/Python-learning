import math

age = {
    'years': '',
    'months': '',
    'days': ''
}

daysTotal = int(input("How old are you by days: "))

years = math.floor(daysTotal / 365) 
months = math.floor((daysTotal % 365) / 30)
days = ((daysTotal % 365) % 30)

age['years'] = years
age['months'] = months
age['days'] = days

print("Years = %s" %years)
print("Months = %s" %months)
print("Days = %s" %days)