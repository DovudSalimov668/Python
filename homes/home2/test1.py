n = int(input())
lst = []
nlst = []
for i in range(n):
    k = input()
    lst.append(k)

for i in range(len(n)):
    for j in range(1,6):
        nlst.append(lst[i]+str(j))