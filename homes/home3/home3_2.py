# text = "My 1 name is Odina . odina : , . is, a developer 1"
# n = text.lower()
# data = n.split()
# res = {} 
# punct = ['.', ',', ':']

# for i in data :
#     if  i in res:

#         res[i] += 1
        
#     else:
#         res[i] = 1
    
# print(res)            





text = "My 1 name is Odina . odina : , . is, a developer 1"
n = text.lower()
data = n.split()
res = {} 
punct = ['.', ',', ':']


for i in data :
    if  punct[i] in data:
        res[i]=""
        
print(res)       
        

# for i in data :
#     if  i in res:

#         res[i] += 1
        
#     else:
#         res[i] = 1
    
# print(res)            