def square(a):
    return a*a

def cube(a):
    return a*a*a

def power(a,b):
    return a**b

def floorDiv(a,b):
    return a//b

print("Basic Calculator")
while True:
    print("1: Square, 2: Cube, 3: Power, 4: Floor Division, 5: Exit")
    n=int(input("Choose an option: "))

    if n==1:        
        print("You've selected Square..") 
        a=int(input("Enter a value: "))     
        print("Square of",a,"is",square(a))
    elif n==2:
        print("You've selected Cube..") 
        a=int(input("Enter a value: "))
        print("Cube of",a,"is",cube(a))
    elif n==3:
        print("You've selected Power..") 
        a=int(input("Enter base value: "))
        b=int(input("Enter power value: "))
        print(a,"^",b,"=",power(a,b))
    elif n==4:
        print("You've selected Floor Division..") 
        a=int(input("Enter 1st value: "))
        b=int(input("Enter 2nd value: "))
        print(a,"//",b,"=",floorDiv(a,b))
    elif n==5:
        print("Thank You. Good Bye")
        break
    else:
        print("Invalid Selection")
