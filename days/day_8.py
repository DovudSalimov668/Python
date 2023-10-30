def prime_num(n,x=2):
    print(x)
    if x==n:
        return True
    elif  n%x==0:
        return False
    else:
        return prime_num(n,x+1)
        
    
    
print(prime_num(11))