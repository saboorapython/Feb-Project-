# end=int(input("Enter a Litre of petrol you want:"))
# end=end+1
# for i in range (1, end+1):
#     print(f"{i}Litre of petrol")
    
    
#odd number:
# for i in range(1,20,2):
#     print(i)


# veg=["tomato", "chilli", "potato", "ladyfinger", "cucumber", "bringal"]
# 
# for i in veg:
#     print(i)


# name=input("Enter your name:")
# for i in name:
#     print(i)


# start=int(input("Enter start"))


# batch
# roll
# courseno
# enrollmentno



batch=int(input("which batch you are creating a package:")) 
std=int(input("How many student are enrolled in this {batch}?:"))
enroll=input("Enter a unique enrollment code:")

for i in range(1,std+1):
    print(f"\n Here are the roll numbers generated for {std} students \nstudent no# {i}-{batch}-{enroll}")



