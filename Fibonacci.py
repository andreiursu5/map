n=int(input("Numarul: "))
a=1
b=1

print(a," ",b, " ")
while a+b<n :
    c=a+b
    a=b
    b=c
    print(c, " ")
    