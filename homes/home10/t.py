import random
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']  
syms = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', "'", '<', ',', '>', '.', '?', '/']
numbers = ['0','1','2','3','4','5','6','7','8','9']
res1 = []
res2 = []
res3 = []
res4 = []
res = []
lengh_1 = int(input("Enter length:"))
print("yes/no")
syms_1 = input("Symbols:")
big_1 = input("Big:")
small_1 = input("Small:")
numbers_1 = (input("Numbers:"))
var = int(input("How many variations do you want: "))

for i in range(1,lengh_1):
    if small_1=='yes':
        res1.append(random.choice(small))
    
for i in range(1,lengh_1):
    if big_1=='yes':
    
        res2.append(random.choice(big))
   
for i in range(1,lengh_1):
    if syms_1=='yes':

        res3.append(random.choice(syms))

for i in range(1,lengh_1):
    if numbers_1=="yes":
   
        res4.append(random.choice(numbers))             
res = res1+res2+res3+res4   

random.shuffle(res)
for i in range(1,lengh_1+1):
    print(str(res[i]),end='')  
# # print(str(res),end='')  
for i in range(1,var+1):
    print(" (",i)
    for j in range(1,len(res)+1):
        random.choice(res)
        print(str(random.choice(res)),end="")
           



