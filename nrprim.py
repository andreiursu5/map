n=int(input("introidu valoarea lui n : "))
ok=1
aux=int(n/2)
for i in range (2,aux,1):
    if n%i==0:
        ok=0
        break
    else:
        ok=1
if ok==1:
       print(n," este prim")
else:
     print(n, " nu este prim")
