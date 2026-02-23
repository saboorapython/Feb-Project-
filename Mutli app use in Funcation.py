# condition loop funcation decision
#     print=int(input("Select an App you want to work: \n1, Calculator \n2. Student Marksheet \n3. Clothing Store \n4. Car Recommendation System"))

print ("******Multiple App Palyer*****")
print("Here are the available apps you can use:\n1. Calculator \n2. Student Marksheet \n3. Cloting Store \n4. Car Recommendation Sysytem \n5. Exit")

# ------------------- FUNCTIONS -------------------
       
def calculator():
    print("Hello {name}, Welcome to the Calculator!")
    while True:
        print("select operator \n1. Addition\n2. Subtraction\n3. Division\n4. Multiply\n5. Exit Calculator")
        select=int(input("select operator (1-5):"))
        
        if select == "5":
            print("Exiting Calculator...")
            break
    
        num1=int(input("Enter number 1: "))
        num2=int(input("Enter number 2:"))
    if select=="1":
        print=(f"Result: {num1+num2}")
    elif select=="2":
        print=(f"Result: {num1-num2}")
    elif select=="3":
        if num2 != 0:
            cal=num1/num2
#     else:
#     print("Cannot divide by zero!")
    elif select=="4":
        print=(f"Result: {num1*num2}")
    else:
        "Worng Input"
        
        
 
    
    
        
    

