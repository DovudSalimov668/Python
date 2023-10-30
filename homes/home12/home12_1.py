import datetime
from datetime import datetime


month_bd = int(input("Enter the month of your birthday: "))
day_bd = int(input("Enter the day of your birthday: "))
hours_bd = int(input("Enter the hour of your birthday: "))
min_bd = int(input("Enter the minutes of your birthday: "))
year_bd = 0
date_string = datetime.now()
format_string = "%m"


mont_now = int(datetime.strftime(date_string,format_string))
if month_bd<=mont_now:
    year_bd = 2024
else:
    year_bd = 2023
   

bd = datetime(month=month_bd,day=day_bd,year=year_bd,hour=hours_bd,minute=min_bd,microsecond=0)
now_time = datetime.today()

res = bd-now_time
print(res)

 