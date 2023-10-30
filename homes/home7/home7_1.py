list1 = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
list2 = []
list2 = list1[0]+list1[1]+list1[2]
list3 = []
resultat = {}
for i in list2 :
    if  i in resultat:
        resultat[i] += 1     
    else:
        resultat[i] = 1

print(resultat) 

   
   