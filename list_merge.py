emp1=int(input("enter emp1 id : "))
emp2=int(input("enter emp2 id : "))
emp3=int(input("enter emp3 id : "))
emp4=int(input("enter emp4 id : "))
emp5=int(input("enter emp5 id : "))

list=[emp1,emp2,emp3,emp4,emp5]
for i in list:
    print(i)
    
sal1=int(input("enter emp1 sal : "))
sal2=int(input("enter emp2 sal : "))
sal3=int(input("enter emp3 sal : "))
sal4=int(input("enter emp4 sal : "))
sal5=int(input("enter emp5 sal : "))

list1=[sal1,sal2,sal3,sal4,sal5]
for i in list1:
    print(i)

print("employee id's and salaries are as below : ")

result=list+list1
for i in result:
    print(i)

    
