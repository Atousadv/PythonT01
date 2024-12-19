
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

#task number eight
# num1=int(input("enter a number:"))
# num2=int(input("enter a number:"))
# sum=num1+num2
# sub=num1-num2
# mult=num2*num1
# div=num1/num2
# print(sum,sub,mult,div)

# task number nine
# num1=int(input("enter a number:"))
# num2=num1**2
# print(num2)

# task number ten
# num1=int(input("enter a number:"))
# if (num1/2 ==0):
#  print("even")
# else:
#     print("odd")

# task number eleven
# import math
# rad=int(input("enter circle's radius:"))
# A=math.pi*rad**2
# print(A)

# task number twelve(compound intrest)
# import math
# principal=float(input("enter pricipal amount:"))
# dur=int(input("enter duration:"))
# A=principal*( (1+0.07)** dur)
# print(A)

# import math
# principal=float(input("enter pricipal amount:"))
# dur=int(input("enter duration:"))
# A=(principal*dur*0.07)/100
# print(A)

# import math
# len=int(input("enter rectangle's length:"))
# wid=int(input("enter rectangle's width:"))
# per=2*(len+wid)
# print(per)

# import math
# n=int(input("how many numbers:"))
# sumofNumbers=0
# for i in range(1, n + 1):
#     num = float(input(f"Enter number {i}: "))
#     sumofNumbers += num
# avg=sumofNumbers/n
# print(avg)

import math
tasks=int(input("how many tasks?"))
perday=int(input("how many tasks per day?"))
hours=int(input("how many hours for the whole project?"))
dur=tasks/perday
work=hours/dur
print(work)

