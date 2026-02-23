def usd(amount):
    return amount * 280   

def euro(amount):
    return amount * 300   

def ringit(amount):
    return amount * 60    # Example rate

def pound(amount):
    return amount * 350   # Example rate

def dihram(amount):
    return amount * 76    # Example rate


while True:
    print("="*50, "Currency Exchange", "="*50)
    cur = float(input("Enter the amount of currency you have: "))
    print("Which Currency Do you want to exchange with Pakistani Rupees: \n1. USD \n2. Euro \n3.Ringit \n4. Pound \n5. Dihram ")
    select = input("Enter your choice (1-5): ")

    if select == "1":
        amt = usd(cur)
        print(f"Here is your converted amount in PKR: {amt}")   
    elif select == "2":
        amt = euro(cur)
        print(f"Here is your converted amount in PKR: {amt}")    
    elif select == "3":
        amt = ringit(cur)
        print(f"Here is your converted amount in PKR: {amt}")    
    elif select == "4":
        amt = pound(cur)
        print(f"Here is your converted amount in PKR: {amt}")   
    elif select == "5":
        amt = dihram(cur)
        print(f"Here is your converted amount in PKR: {amt}")    
    else:
        print("Wrong input! Please select between 1-5.")
    rerun = input("Do you want to continue? (yes/no): ").lower()
    if rerun == "yes":
        continue
    else:
        print("Thank you for using Currency Exchange Program")
        break