#Functions in python!

# def calc(num1, num2,num3,num4): #positinal argoments(num1+num2)
#     add=num1-num2+num3-num4
#     return print(f"This is Addition:{add}")
# 
# 
# calc(50,100,500,78)


# def calc():
#     num1=eval(input("Enter no# 1:"))
#     num2=eval(input("Enter no# 2:"))
#     sub=num1-num2
#     add=num1+num2
#     mul=num1*num2
#     div=num1/num2
#     select=input("what you want? \n1.Addition \n2.Subtraction \n3.multipiclication \n4.divided:")
#     if select=="1":
#         cal=num1+num2
#     elif select=="2":
#         cal=num1-num2
#     elif select=="3":
#         cal=num1*num2
#     elif select=="4":
#         cal=num1/num2
#     else:
#         cal="Worng Input!"
#     return print(cal)    
# 
# 
# calc()





# def calc(num1,num2,opr):
#     if opr=="+":
#         cal=num1+num2
#     elif opr=="_":
#         cal=num1-num2
#     elif opr=="/":
#         cal=num1/num2
#     elif opr=="*":
#         cal=num1*num2
#     else:
#         cal="Worng input"
#     return print(cal)
# 
# 
# calc(50,100,"*")


# def calc(num1,num2,opr):
#     if opr=="+":
#         cal=num1+num2
#         var="Addition"
#     elif opr=="-":
#         cal=num1-num2
#         var="Subtraction"
#     elif opr=="/":
#         cal=num1/num2
#         var="Division"
#     elif opr=="*":
#         cal=num1*num2
#         var="Multiplication"
#     else:
#         cal="Worng input"
#     return print(f"This is {var} of {num1} and {num2} which is:{cal}")
# 
# calc(50,100,"/")


def calc():
    while True:
        num1=int(input("Enter number 1:"))
        num2=int(input("Enter number 2:"))
        opr=input("Enter operator: +, -, *, / :")
        if opr=="+":
            cal=num1+num2
            var="Addition"
        elif opr=="-":
            cal=num1-num2
            var="Subtraction"
        elif opr=="/":
            cal=num1/num2
            var="Division"
        elif opr=="*":
            cal=num1*num2
            var="Multiplication"
        else:
            cal="Worng input"
        print(f"This is {var} of {num1} and {num2} which is:{cal}")
        rerun=input("Do you want to continue?: (yes/no):").lower()
        if rerun=="yes":
            continue
        else:
            break
        print(f"This is {var} of {num1} and {num2} which is:{cal}")


calc()