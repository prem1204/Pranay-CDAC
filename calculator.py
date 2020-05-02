def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print("Basic Calculator")
while True:
    print("1: Add, 2: Subtract, 3: Multiply, 4: Divide, 5: Exit")
    n=int(input("Choose an option: "))

    if n==1:        
        print("You've selected Addition..") 
        a=int(input("Enter 1st value: "))
        b=int(input("Enter 2nd value: "))       
        print(a,"+",b,"=",add(a,b))
    elif n==2:
        print("You've selected Subtraction..") 
        a=int(input("Enter 1st value: "))
        b=int(input("Enter 2nd value: "))
        print(a,"-",b,"=",sub(a,b))
    elif n==3:
        print("You've selected Multiplication..") 
        a=int(input("Enter 1st value: "))
        b=int(input("Enter 2nd value: "))
        print(a,"*",b,"=",mul(a,b))
    elif n==4:
        print("You've selected Division..") 
        a=int(input("Enter 1st value: "))
        b=int(input("Enter 2nd value: "))
        print(a,"/",b,"=",div(a,b))
    elif n==5:
        print("Thank You. Good Bye")
        break
    else:
        print("Invalid Selection")
