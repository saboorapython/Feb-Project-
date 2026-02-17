print("*********Wedding Hall Recommendation System**********")

name=input("Enter your name:")
budget=int(input("Enter your budget:"))
seats=int(input("Enter you budget:"))
ac=input("Do you need AC?(yes/no):").lower()
carparking=input("Enter Parking (yes/no):")
halltype=input("Enter your hall type (indoor/outdoor):")

if budget<=500000 and seats<=300 and ac== "yes" and carparking== "yes" and halltype== "outdoor":
    print(f" Dear {name}, your recommendation hall type \n1.Local Marriage Lawn \n2.Community Center Hall \n3.Simple Banquet Lawn")
if budget<=1200000 and seats<=500 and ac== "yes" and carparking== "yes" and halltype== "Indoor":
    print(f" Dear {name}, your recommendation hall type \n1.Royal Banquet \n2.Pearl Wedding Hall \n3.Elegant Marquee")
if budget<=2500000 and seats<=800 and ac== "yes" and carparking== "yes" and halltype== "Iutdoor":
    print(f" Dear {name}, your recommendation hall type \n1.Dream Banquet \n2.Grand Palace Hall \n3.Luxury Marquee")
else:
    print(f" Dear {name}, Recommendation big hall avaliable: \n1. Expo Center Banquet \n2. 5 Star Hotel Ballroom \n3. Premium Event Complex")
          
         