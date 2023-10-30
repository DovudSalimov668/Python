'''
1)  
def power(a,b):
    if b==1:
        return a
    else:
        return power(a,b-1)*a
print(power(10,20))  
2)
def dict_pow(n=5):
    dictionary = {}
   
    for i in range(1,n+1):
        
            dictionary[i] = i*i
    return dictionary
            
            
print(dict_pow(10))    
3)
data_1, data_2 = {1: 1, 2: 4, 3: 9}, {4: 16, 5: 25, 6: 36}

print(data_1 | data_2)  
# 5)x = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# print(x.items())
    

'''