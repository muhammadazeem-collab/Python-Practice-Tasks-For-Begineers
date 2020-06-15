1. Simple Python Calculator

#It will take first number from user
number_1 = int(input("Enter first number:")) 

#It will take second number from user
number_2 = int(input("Enter second number:"))

#User have to choice heir desire operation
choice =  int(input("Choice Operation: * 1 == Addition * * 2 == Subtraction * * 3 == Multiplication * * 4 == Division *"))

#Conditional Statement is Used

if choice == 1:
    print("Addition is performed. Result = ",number_1 + number_2)
elif choice == 2:
    print("Subtraction is performed. Result =",number_1 - number_2)
elif choice == 3:
    print("Multiplication is performed. Result =",number_1 * number_2)
elif choice == 4:
    print("Division is performed. Result =",number_1 / number_2)
else:
    #If user enter invalid number's
    print("Invalid Input's")