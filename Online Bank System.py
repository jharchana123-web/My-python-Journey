import time

name = (input("Hello, Let's go for verification!\n What is your name: "))
a = int(input("Please fill your account No.: "))

pin = 5555
Attempets = 3
while Attempets > 0:
    Pin = int(input("Enter pin: "))
    if pin == Pin:
        print(f"Hello {name}, Account access Granted!")
        break

    else:
        Attempets = Attempets - 1
        print (f"============!Warning!==========\n Your account can Be blocked for 24hrs.")

if Attempets == 0:
     print(f"{name}, you are blocked for 24 hrs")
     exit()

Balance = 2000
Cibil_Score = 750
History = [1200,2506,8000,3002,2300,5412,8700,98700]

print("Waiting for a while......")
time.sleep(3)  # Accepts floats too, like 0.5 for half a second

print ("1. Check Your Balance")
print ("2. Check Your History")
print ("3. Check Your Cibil Score")
print ("4. Check Your Deposit")
print ("5. Exit ")
Choice = int(input("What do you want to do: "))

if Choice == 1:
    print(f"Your balance is: {Balance}")

elif Choice == 2:
    print(f"Your History is printed here: {History}")

elif Choice == 3:
    print(f"Your Cibil Score is well\n Your score: {Cibil_Score} ")

elif Choice == 4:
    amount = int(input("Enter amount to deposit: $ "))
    
    Money = (f"{Balance} = {Balance} + {amount}")

    History.append(f"Deposited: +₹{amount}")
        
    print(f" Successfully Credited! ₹{amount} added to your account.")

else:
    print ("===========OK! By sir. Have a nice day!====================")




    if Attempets == 0:
        print(f"Sorry, {name} Your account is blocked.")    