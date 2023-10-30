from my_module1 import calculator1
from dict import history
print("============================= Calculator ======================================================")

# a  = int(input("enter num1:"))
# b =  int(input("enter num2:"))
x = input("Enter number_symbol(or log)_number: ").split()
a = int(x[0])
b = int(x[2])
c = ["+","-","*","/","**","log","log1"]
c = (x[1])

# c = str(input("Enter symz:"))
calculator1(a,b,c)
run = True
while run:
     exp  =  input("entrr")
     if exp in history:
          print("yes")
     elif exp  == "q":
          break
     elif exp =="p":
          print(history)    
     else:
          calculator1         