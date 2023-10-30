# namecopy = ""
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
# list2 = [2, 4, 6, 8]
# str(list1)
# str(list2)
# str(namecopy)




# for i in range(len(list1)):
#     if list1[i] in list2:
#         continue
#     else :
#         namecopy=namecopy+list1[i]

# print(namecopy)

# x =  ['4', '12', '45', '7', '0', '100', '200', '-12', '-500'] 
# y = [-500, -12, 0, 4, 7, 12, 45, 100, 200]

# print(sorted(y))
# print(sorted(x))
# x =[['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]

# revlist = x.reverse()
# print(revlist)
# x = int(input('length:'))
# y = int(input('width:'))
# res = ()
# def calculate_area(x,y):
#     res=x*y
#     print(res)

# calculate_area(x,y)
# str = input('number:')
# try: 
#     x = int(str)
# except: 
#     x = 10
# if x == 10 :  
#     print('=')
# else:  
#     print('Not =10')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]
list3 = []


# for i in range(len(list1)):
#     if (list1[i] in list2):
#         continue
#     else :
#         list3.append(list1[i])

# print(list3)

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [2, 4, 6, 8]
# result = []
# for i in list1:
#     if i not in list2:
#         result.append(i)
# print(result)
alllist = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]

listset = []

for i in range(len(alllist[2])):
    if alllist[2][i] not in alllist[0] and alllist[1]:
        continue
    else :
        listset.append(alllist[2][i])

print(listset)