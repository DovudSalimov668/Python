# user_input =  int(input("enter the year: "))
# if user_input%4==0 and user_input%100!=0 or user_input%400==0 :
#     print(user_input)
#     print("true")
# else:
#     print("ne visokosni")    
# import datetime
# from datetime import datetime
# date_string = datetime.now()
# format_string = "%d"
# today_day = datetime.strftime(date_string,format_string)

# print("Yesterday:",int(today_day)-1)
# print("Today:",today_day)
# print("Tomorrow:",int(today_day)+1)

# import datetime
# from datetime import datetime
# date_string = datetime.now()
# format_string = "%d-%m-20%y"
# print(datetime.strftime(date_string,format_string))
# form_str_day= "%d"
# form_str_month = "%m"
# form_str_year = "%y"
# var1 = int(datetime.strftime(date_string,form_str_day))

# print("Result: ",var1-5)
# print("Result: ",var1-5,"-",datetime.strftime(date_string,form_str_month),'- 20',datetime.strftime(date_string,form_str_year))

# import datetime
# day = datetime.date.today()
# substract = datetime.timedelta(days=-5)
# print(day+substract)

# import datetime
# from datetime import datetime


# day_input1 = int(input("Enter the day1 : "))
# month_input1 = int(input("Enter the month1 : "))
# year_input1 = int(input("Enter the year1 : "))

# day_input2 = int(input("Enter the day2 : "))
# month_input2 = int(input("Enter the month2 : "))
# year_input2 = int(input("Enter the year2 : "))

# user_input1 = datetime(month=month_input1,day=day_input1,year=year_input1)

# user_input2 = datetime(month=month_input2,day=day_input2,year=year_input2)

# print(user_input2-user_input1)
# prices = [7,1,5,3,6,4]
# print("day_1: ",prices[0])
# print("day_2: ",prices[1])
# print("day_3: ",prices[2])
# print("day_4: ",prices[3])
# print("day_5: ",prices[4])
# print("day_6: ",prices[5])
# user_input1 = int(input("Enter the day for buying"))
# user_input2 = int(input("Enter the day for selling"))
# val = 0
# res = 0
# if user_input1==1:
#     val = prices[0]
# elif user_input1==2:
#     val = prices[1]
# elif user_input1==3:
#     val = prices[2]  
# elif user_input1==4:
#     val = prices[3] 
# elif user_input1==5:
#     val = prices[4] 
# elif user_input1==6:
#     val = prices[5]   
# else:
#     val = 0        


# val1 = 0

# if user_input2==1:
#     val1 = prices[0]
# elif user_input2==2:
#     val1 = prices[1]
# elif user_input2==3:
#     val1 = prices[2]  
# elif user_input2==4:
#     val1 = prices[3] 
# elif user_input2==5:
#     val1 = prices[4] 
# elif user_input2==6:
#     val1 = prices[5]     
# else:
#     val1 = 0     

# print(val-val1)
# import pathlib

# input_file_name = input("Enter file name: ")
# input_num = int(input("enter nums of lines: "))
# input_file_name_1 = pathlib.Path(input_file_name)
# print(input_file_name_1)
# cwd_1 = pathlib.Path.cwd()
# file_path = cwd_1 / input_file_name_1
# with open(file_path, "r") as file:
#             content = file.read()
#             print("Content:")
#             print(content)
              

# import datetime
# day = datetime.date.today()
# substract = datetime.timedelta(days=-5)
# print(day+substract)
import pathlib
user_input_file = input("Enter name of file: ") 
user_file = pathlib.Path(user_input_file)
user_input_lines = int(input("Enter how many lines you want too see?: "))
f = open(user_file)
for line in f.readlines():
    for i in range(1,user_input_lines+1):
        print(line,end='')
f.close()

