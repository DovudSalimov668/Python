
import datetime
from datetime import date,time,datetime
# print(datetime.now() )
date_string = datetime.now()
format_string = "%m"
print(datetime.strftime(date_string,format_string))

