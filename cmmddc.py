a=int(input("introidu valoarea lui a: "))
b=int(input("introidu valoarea lui b: "))
while a!=b:
    if(a>b):
        a=a-b
    else: 
        b=b-a
print("cmmdc este ",a)