def evenOdd(x):
    if(x%2==0):
        print("even")
    else:
        print("odd")
evenOdd(10)
def firstNameLasrName(x,y):
    print("first name is ",x)
    print("last name is ",y)
firstNameLasrName("bhagyalaxmi","palai")  
#types of phython function arguments
#1.Default argument
#2.Keyword argument
#3.Positional argument
#4.Arbitary Keyword argument
def type(fname,age):
    print("first name:",fname)
    print("age is:",age)
type("bhagya",20)
type(21,"bhagya")
type(age=24,fname="bhagya")


