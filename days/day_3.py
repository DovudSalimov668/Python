# txt = dict()
# print('text:')
# line = input('')

# words = line.split()
# print(words)
# for i in words:
#     if 
    


# """

# dict = {
# "my": 1,
# "dovud": 2,
# }
# """


text = "My name is Dovud, dovud"

data = text.split()
res = {}
for i in data:
    if i in res:
        res[i] += 1
    else:
        res[i]=1

print (res)
    
