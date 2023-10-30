import random
pols = input("Enter your password: ")
pols_1 = pols
small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
res = list(pols_1)
while res!=pols:
    
    res = random.shuffle(list(pols))
    print(pols)