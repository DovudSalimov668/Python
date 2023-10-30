"""
1) Virtualenv eto instrument blagodarya , kotoromu mi mozhem nastroit nash proekt. Mi mozhem vibrat nuzhnuyu versiyu Python kotaray ne budet zatragivat drugie proekti.
dlya zapuska venv ns nashom proekte nuzhno zapustit v terminale opredelennuyu komandu ,a potom sozdat papku vnutri proekta dlay ee activacii.


2) Различие между выражением и оператором в Python zakluychayutsya v tom chto virazhenie v sebe ispolzuet znacheniay i operatori odnovremenno ,rezultat kotorih mozhno prisvoit peremrnnoi. (1+4-x). Operatori vipolnyayut razlichnie zadachi. Slozhenie i td (= == - + > < >= <=)
3)x = int(input())

if x%2==0:
    print('«Четное число»')
else:
    print('«Нечетное число»' )

    
6)for i in range(1,11):
    print(i, end=" ")
9) Назначение функции range() zaklyuchaetsau v tom chtobi poschitat dlinu dopustim lista po indeksu vkluychitelno
x = []
for i in range(1,6):
    x.append(i)
print(x)
10)list1 =  [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17] 
list2 = [2, 4, 6, 8, 10, 12, 14]

for i in list1:
    for j in list2:
        if i==j:
            print('True')
        else:
            print('False')  
  15)x =  ['4', '12', '45', '7', '0', '100', '200', '-12', '-500'] 
y = [-500, -12, 0, 4, 7, 12, 45, 100, 200]

print(sorted(y))
print(sorted(x))
16)x =[['white', 'black', 'pink'], ['green', 'blue'], ['orange', 'red']]
revlist = x.reverse()
print(revlist)
7)x = int(input('length:'))
y = int(input('width:'))
res = ()
def calculate_area(x,y):
    res=x*y
    print(res)

calculate_area(x,y)
4)
str = input('number:')
try: 
    x = int(str)
except: 
    x = 10
if x == 10 :  
    print('=')
else:  
    print('Not =10')
5)matchcase vipolnayet odni i tezhe funcii kak i if i else i elif
ego mozhno ispolzovat vmesto if i else
8)list[]mutable 
dict{} poradok zavisit ot poraydka zapisi v dict
tuple() unmutable znacheniay dont repeat
set() ne mozhet soderzhat dublicati


"""
list = [1,2,3,4,5,6]
res  = ()
for i in list:
    print(i,end=' ') 
    