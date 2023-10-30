# def num_count(n):
#     # cnt = 0
#     # print(n)
#     if  n<10:
#         return 1
#     else:
        
#         return num_count(n/10)+1
#             #  cnt+=1

# print(num_count(999))


   
   


def num_count(n):
    
    if  n<10:
        return 1
    else:
        
        return num_count(n[:-1])
           

print(num_count(999))