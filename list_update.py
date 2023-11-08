emp1=int(input("enter emp1 id : "))
emp2=int(input("enter emp2 id : "))
emp3=int(input("enter emp3 id : "))
emp4=int(input("enter emp4 id : "))
emp5=int(input("enter emp5 id : "))
list=[emp1,emp2,emp3,emp4,emp5]
for i in list:
    print(i)
p=int(input("enter position of index"))
rp=int(input("enter empid which you want to replace: "))
list[p]=rp
for i in list:
    print(i)
