n=int(input())
nlist=list(map(int, input().split()))

max=nlist[0]
min=nlist[0]

for i in nlist[1:]:
    if i>max:
        max=i
    elif i<min:
        min=i

print(min,max,end=" ")
    