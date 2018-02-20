while True :
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    
    if a == 0:
        r = -c / b
        print("root = ", r)
    else:
        t = b**2 - 4*a*c

        r1 = (-b - t**0.5)/(2*a)
        r2 = (-b + t**0.5)/(2*a)

        print("roots = ", r1, ",", r2)
