#funcation in python: is a modular programming in python
#(funcation banatye hain , templeates , modules bantye hain.....)

#user defined modules in python

def saboora():
    select=input("what you want to use? \n1.calc \n2.marksheet \n3.nothing")
    if select=="1":
        num1=int(input("Enter a number 1:"))
        num2=int(input("Enter a number 2:"))
        print(f"This is Addition:{num1+num2} \nThis is Subtraction:{num1-num2} \nThsi is Division:{num1/num2} \nThis is Multiplication: {num1*num2}")
        
    elif select=="2":
        obtain=int(input("Enter your obtain marks:"))
        total=500
        per=(obtaib/total)*100
        if pr>=70:
            grade="A+"
        else:
            grade="Fail"
        print(grade)
        
        
saboora()        