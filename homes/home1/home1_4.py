a = 25
b = 50
for i in range(a,b+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
         print(i)