# numberlist = ['p','q']
# x = int(input())

# for i in range(1,x+1):
    
#     numberlist.append(numberlist[0]+str(i))
#     numberlist.append(numberlist[1]+str(i))
# print(numberlist)

a = [4,5,67,364,47,6]
b = [4,7,67,34,4,6]
x = []
for i in a:
    for j in b:
        if i==j:
                 x.append(i)
   
print(x)        
