text = "My n2ame 1 is 3 Odina , odina is : , developer."
text_cleared  = []

res = {}
panctuations = [".",",",":"]
data = text.lower().split()

for i in data:
    try:
       a = i.split(".")
       print(a, end=' ')
    except:
       pass
    
    if i.isalpha() or i.isdigit() or i.isalnum():
       if i in res:
        res[i] += 1
    else:
        res[i] = 1 
           
print(res)        