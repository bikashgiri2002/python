# Enter three number find bigest
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))
if a>b:
    if a>c:
        print(a," is big")
    else:
        print(c,"is big")
else:
    if b>c:
        print(b," is Big")
    else:
        print(c," is Big")