import math
dict_history = {}

def log(a,b):
    i = 1 
    counter = 0
    while True:
        i = i * a
        counter += 1
        if i == b :
            break
    return counter

def calculator1(a,b,c):
    
    match c:
        case "+":
            y = a+b
            print("answer:",y)
        case "-":
            y = a-b
            print("answer:",y)
        case "*":
            y = a*b
            print("answer:",y)
        case "/":
            y = a/b
            print("answer:",y)
        case "**":
            y = a**b
            print("answer:",y)
        case "log":
            y = log(a,b)
            print("answer:",y) 
        case "log1":
            y = math.log(b,a)
            print("answer:",y)     
# dict_history.update(x,y)      
           



