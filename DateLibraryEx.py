
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

#task number five
# from datetime import datetime, timedelta

# date_str = input("Insert a date (YYYY-MM-DD): ")
# days = int(input("Insert a number of days: "))

# date_obj = datetime.strptime(date_str, "%Y-%m-%d")
# new_date = date_obj + timedelta(days=days)

# print(new_date.strftime("%Y-%m-%d"))

# task number six
# from datetime import datetime
# month=int(input("tell me a month(1-12):"))
# year=int(input("tell me a year:"))
# firstday=datetime(year,month,1)
# weekday=firstday.strftime("%A")
# print(weekday)

# task number seven 
# import calendar
# year=int(input("insert a year:"))
# if calendar.isleap(year):
#  print(f"{year}is leap")
# else:
#  print(f"{year} is not a leap year")

import calendar
year = int(input("Enter the year (e.g., 2024): "))
month = int(input("Enter the month (1-12): "))
first_day, _ = calendar.monthrange(year, month)
if first_day == 6:
    print(f"The first of {calendar.month_name[month]} {year} is a Sunday.")
else:
    print(f"The first of {calendar.month_name[month]} {year} is not a Sunday.")
