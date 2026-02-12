#loops in pyhton!
# "for"step ke acording chalta hai.
# membership operator (is, in)
# range 0, continuse hoga.
# for loop automatic count karta hain.

# range funcation:
    
# for hello in range(1, 10, 2):  
#     print (hello)
    
num1=int(input("Enter a number for table:"))
for i in range (1, 11):
    print(f"{num1} * {i} = {i*num1}")
    
    
# range funaction in for loop!
# -by default sop if it looks like range(5):
# - range (start, stop)
# - range (start, stop, step)




while True:
    num1=int(input("Enter a number for table:"))
    for i in range(1, 11):
        print(f" {num1} * {i} = {i*num1}")
    rerun=int(input("Do you want to print another table? \nPress 1. for Yes \nPress 2. No \n:"))
    if rerun==1:
        continue
    else:
        print("Thank you!")
        break