
# task number one

# import datetime
# age=int(input("what is your birth year:?"))
# currentDate=int(input("what is current date?"))
# x=int(currentDate-age)
# print(x)

#task number two
# from datetime import datetime
# date=input("insert a date:")
# date_object=datetime.strptime(date,"%Y-%m-%d")
# week_day=date_object.strftime("%A")
# print(week_day)

#task number three
# import calendar
# year=int(input("insert a year:"))
# print(calendar.calendar(year))

import calendar
month=int(input("tell me a month:"))
year=int(input("tell me a year:"))
print(calendar.month(year,month))
