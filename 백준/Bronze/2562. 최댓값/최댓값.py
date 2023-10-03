nlist=[]

for i in range(9):
    nlist.append(int(input()))
    
print(max(nlist))
print(nlist.index(max(nlist))+1)