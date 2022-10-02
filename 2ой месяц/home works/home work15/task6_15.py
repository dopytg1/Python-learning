def date_format(birthday):
   birthday_list = birthday.split('/')
   months = [" ", "January", "February", "March", "April", "May", "June", "July", "August","September", "October", "November", "December"]
   print("You were born in %s, %s of %s" %(birthday_list[2], birthday_list[0], months[int(birthday_list[1])] ))


birthday = input("Enter your birthday in дд/мм/гггг format: ")
date_format(birthday)