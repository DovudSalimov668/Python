import pathlib
import os 
user_file = input("Enter name of the file: ")
cur_path = pathlib.Path.cwd()
n_file = pathlib.Path(user_file)
# n_file = os.path.abspath(user_file)
cur_p = cur_path / n_file
print(cur_p)

# # print(cur_p)
# # fhand = open(cur_p,"r")
# # count = 0
# # for line in fhand:
# #     count = count + 1
# # print('Line Count:', count)
input_num = int(input("Enter number of lines: "))
open(cur_p,"r")

for i in range(1,input_num+1):
    print(cur_p.readlines())
