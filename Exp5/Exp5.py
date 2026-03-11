def calc(x, y):
    return x + y, x - y

n = int(input("Enter choice:\n1. Calculate\n2. Exit\n"))

if n == 1:
    x = int(input("enter x: "))
    y = int(input("enter y: "))
    
    s, p = calc(x, y)
    
    print("X + Y: ", s)
    print("X - Y: ", p)

elif n == 2:
    print("Exiting")

else:
    print("invalid input")