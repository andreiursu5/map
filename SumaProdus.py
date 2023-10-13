n=int(input("Nr de termeni din lista: "))
s=0
p=1
for i in range(0,n,1):
    x=int (input())
    s=s+x
    p=p*x

print("Suma nr este: ", s)
print("Produsul nr este: ", p)