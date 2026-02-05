a = float(input("Enter the first number"))
b = float(input("Enter the second number"))
c = float(input("Enter the third number"))

if a >= b and a >= c:
    print("First number is largest", a)
elif b >= a and b >= c:
    print("Second number is largest", b)
else:
    print("Third number is largest", c)

