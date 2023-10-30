# data = [(2,7),(2,6),(1,8),(4,9)]
# mx  = data[0][0] * data[0][1]
# mn = data[1][0] * data[1][0]
# for i in range(len(data)):
#     temp_1 = data[i][0] * data[i][1]
    
#     if temp_1 > mx:
#         mx = temp_1
# print("max: ",mx ,"min: ", mn)    

# x = ['Python', 'Exercises', 'Practice', 'Solution', 'Exercises', 'Exercises', 'Exercises']

# for value in x:
#     if x.count(value) > 1:
#         x.remove(value)

# print(x)
ls = ['4', '12', '45', '7', '0', '100', '200', '-12', '-500']
new_ls = []
for i in ls:
    new_ls.append(int(i))
print(sorted(new_ls))