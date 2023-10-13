import math 
a=int(input("Primul numar: "))
b=int(input("al doilea nr: "))
c=int(input("al 3lea nr: "))
d=b*b-4*a*c
y=0
if d>0:
    x=((-b)+math.sqrt(d))/2*a
    y=((-b)-math.sqrt(d))/2*a
    print("x este ", x)
    if y!=0:
     print("y este ", y)
if d==0:
 x=-b/2*a
print("x este ",x )