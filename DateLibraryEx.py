
# task number one

# import datetime
# age=int(input("what is your birth year:?"))
# currentDate=int(input("what is current date?"))
# x=int(currentDate-age)
# print(x)

from datetime import datetime
date=input("insert a date:")
date_object=datetime.strptime(date,"%Y-%m-%d")
week_day=date_object.strftime("%A")
print(week_day)