a = float(input("a = "))
x = 1
while abs(x**2 - a) > 1e-8 :
    x = (x+a/x)/2

print(x, a**0.5)