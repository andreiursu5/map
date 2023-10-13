n=int(input("Nr de numere din lista: "))
x=int(input())
min=x
max=x

for i in range(1,n,1):
    x=int(input())
    if x<min:
        min=x
    elif x>max:
        max=x

print("Max= ",max)
print("Min=", min)
