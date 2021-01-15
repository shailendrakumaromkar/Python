import datetime

print(datetime.datetime.now())
print(datetime.datetime.now().year)
print(datetime.datetime.now().strftime("%A"))

today=datetime.datetime(2020,1,15)
print(today)
print(today.strftime("%B"))