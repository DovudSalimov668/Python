def nat_num(n):
    if n==1:
        return 1
    else:
        return nat_num(n-1)+n
n = int(input("Enter your number:")) 
print("Sum the first n natural numbers:", end=' ')  
print(nat_num(n))    