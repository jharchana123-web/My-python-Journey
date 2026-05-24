print ("================Welcome To My Expense Tracker==================")

Name = input("What is your name: ")
Gender = input("What Can I Call You (Male/Female): ")
if Gender == "female":
    print(f"Shu Swagatam Shrimati {Name} Ji!")
elif Gender == "male":
    print(f"Shu Swagatam {Name} Ji!")
else:
    print(f"Welcome {Name}!")
     
print (f"################## What Are You Want To Do {Name} ########################")

history = []

while True:
    print ("1. Add Newe Expense ")
    print ("2. Check Balance")
    print ("3. Check History")

    Choices = int(input("What do you want to do: "))

    if Choices == 1:
        print ("Let us add!")
        items = input("What do you buy: ")
        price = int(input(f"Price of the {items}: "))
        date = input("Date of purchase: ")
        history.append({"item": items, "price": price, "date": date})
        print("Expense added successfully!")

    elif Choices == 2:
        total_expense = 0
        for entry in history:
            total_expense += entry["price"]
        print (f"Your total amount spent is: {total_expense}")
        print (f"Thanks! for coming here {Name} ")
        
    elif Choices == 3:
        print(f"\n--- Expense History for {Name} ---")
        if not history:
            print("No history found.")
        else:
            for i, entry in enumerate(history, 1):
                print(f"{i}. {entry['date']} | {entry['item']} | Price: {entry['price']}")
        print("-----------------------------------\n")
