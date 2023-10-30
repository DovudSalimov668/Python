
import random
# print(random.getrandbits())
lst_pw = []
abc123 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']  
syms = ['~', '`', '!',  '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|', ':', ';', "'", '<', ',', '>', '.', '?', '/']

for i in range(1,100):
 
    lst_pw.append(random.randint(1,10))
  
    lst_pw.append(i)
    lst_pw.append(random.choice(syms))
    lst_pw.append(random.choice(abc123))
    
for i in range(1,len(lst_pw)):
    print(str(lst_pw[i]),end='')


