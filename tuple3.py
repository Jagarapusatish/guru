tel=int(input("enter tel marks : "))
hin=int(input("enter hin marks : "))
eng=int(input("enter eng marks : "))
maths=int(input("enter maths marks : "))
sci=int(input("enter sci marks : "))
soc=int(input("enter soc marks : "))

stdmarks=(tel,hin,eng,maths,sci,soc)
print(stdmarks)
s=int(input("enter the first index position : "))

print(stdmarks[:s])
