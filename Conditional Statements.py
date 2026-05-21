Name = input("What is your name user? ")
print (f"Hello, Let's check your threat score {Name}: ")

Threat_Score = int(input("Give your score: "))

if Threat_Score >= 70:
    print (f"Your Score is dangerous {Name}: ")

elif Threat_Score >= 50:
    print (f"I can't open your score is sensetive. I am sorry,{Name}")

else:

    print (f"Welcome {Name}, Your acess granted! Enjoy your Calculator! ")

    print("===========Welcome To My Calculator===========")
    import math

    print (f"What do you want to do {Name}? ")

    print ("Please Choose One Option: ")
    print ("1. Squre Root")
    print ("2. Exponents")
    print ("3. Round Up")
    print ("4. Round Down")

    Choice = int(input(f"Choose one option {Name}: "))

    if Choice == 1:

        num = float(input("Enter number: "))
        result = math.sqrt(num)
        print (f"Your answer is: {result}")

    elif Choice == 2:
        base = float(input("Enter your number: "))
        exponent = float(input("Enter power/exponent: "))
        result = math.pow(base,exponent)
        print (f" {Name}your answer is:{result}")

    elif Choice == 3:
    
        num = float(input("Enter a decimal number to round UP: ")) # It is used for round up.
        result = math.ceil(num)
        print(f"Ceiled Value: {result}") 

    elif Choice == 4:
    
        num = float(input("Enter a decimal number to round DOWN: ")) # It is used for round down the numbers. 
        result = math.floor(num)
        print(f"Floored Value: {result}")    

