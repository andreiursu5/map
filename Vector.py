v=[]
for i in range (8):
    x=int(input(str(i)))
    v.append(x)
ok=0
for i in range (7):
    for j in range (7-i):
        if v[j]>v[j+1]:
            ok=1
            v[j]=v[j+1]
            v[j+1]=v[j]

for i in range(8):
    print(v[i]," ")

