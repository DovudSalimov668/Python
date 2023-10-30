
import random

pols = input("Enter your password: ")
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
aplha = small+numbers

g_pass = ''
attempts = 0

while g_pass != pols:
    g_pass = ''.join(random.sample(aplha, len(pols)))
    print(g_pass)
    attempts += 1

print(g_pass)
  
