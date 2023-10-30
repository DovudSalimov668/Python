text = "My 1 name is Odina . odina : , .is, a developer 1"
n = text.lower()
data = n.split()
res = {}
for i in data :
    if  i in res:
        res[i] += 1     
    else:
        res[i] = 1
print(res) 