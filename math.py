import math

# to calculate power
n=int(input("enter base number"))
p=int(input("enter power number"))
x=math.pow(n,p)
print(x)

# to calculate square root

print(math.sqrt(n))

# to get max number

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
print("maximum value is :",max(a,b,c))

# to get min number
print("minimum value is :", min(a,b,c))

# to get pi value

print(math.pi)

# to print next integer of the given float value
d=float(input("enter the value"))
print(math.ceil(d))

# to print previous integer of the given float value
f=float(input("enter the value"))
print(math.floor(d))

# trigonometric operations

ang=int(input("enter the angle"))
print(math.cos(ang))
print(math.sin(ang))
print(math.tan(ang))
print(math.sec(ang))
print(math.cosec(ang))
print(math.cot(ang))
