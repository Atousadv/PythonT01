
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

# task number four
# import calendar
# month=int(input("tell me a month:"))
# year=int(input("tell me a year:"))
# print(calendar.month(year,month))

from datetime import datetime, timedelta

date_str = input("Insert a date (YYYY-MM-DD): ")
days = int(input("Insert a number of days: "))

date_obj = datetime.strptime(date_str, "%Y-%m-%d")
new_date = date_obj + timedelta(days=days)

print(new_date.strftime("%Y-%m-%d"))