# Find Maximum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if(a>b and a>c):
    print("The highest number is", a)
elif(b>a and b>c):
    print("The highest number is", b)
elif(c>a and c>b):
    print("The highest number is", c)
elif(c==a and b==c):
    print("All values are equal")
