#sets
emp1=int(input("enter emp1 id : "))
emp2=int(input("enter emp2 id : "))
emp3=int(input("enter emp3 id : "))
emp4=int(input("enter emp4 id : "))
emp5=int(input("enter emp5 id : "))
emp={emp1,emp2,emp3,emp4,emp5}

print(type(emp))

print(len(emp))

emp.pop() #pop deletes first value from the set
for i in emp:
    print(i)

emplt=list(emp) # converted into list since in set update is not possible
index=int(input("enter index value"))
va=int(input("enter id to replace"))
emplt[index]=va
for i in emplt:
    print(i)

ad=int(input("enter id to add"))
emp.add(ad)
for i in emp:
    print(i)
