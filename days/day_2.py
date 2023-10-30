numlist = [1,2,3,4,5,6,7,8,9,10]
x = numlist[0]
for i in range(10,len(numlist),2 ):
    if x < numlist[i]:
        x = numlist[i]
print(x)

