print("Welcome to the goofy ahh arithmetic calculator")
first= float(input("enter the first number"))
operator=input("enter an operator(*,+,-,/):")
second= float(input("enter the second number"))
if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*" :
    print(first*second)
elif operator=="/":
    if second==0:
        print("not today son")
    else:print(first/second)


else: print("TF do you want me do to????")




